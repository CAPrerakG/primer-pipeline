# One-time generator for sections.json (the canonical status file for all 278 sections).
# After seeding, agents edit sections.json directly (status/primer) and run mkchecklist.py.
# Re-running this would reset queue order and notes, so it refuses if sections.json exists
# unless called with --force.
import json, io, os, sys, collections

if os.path.exists('sections.json') and '--force' not in sys.argv:
    sys.exit('sections.json already exists; edit it directly, or pass --force to regenerate.')

# 1) normalise urls.json to full URLs (069-078 were saved as bare ids by mistake)
u = json.load(io.open('urls.json', encoding='utf-8'))
for k, v in u.items():
    if not v.startswith('http'):
        u[k] = 'https://claude.ai/artifact/' + v
json.dump(u, io.open('urls.json', 'w', encoding='utf-8'), indent=1)

b = json.load(io.open('../base.json', encoding='utf-8'))
cnt = collections.OrderedDict(); wl = {}
for r in b:
    cnt[r['ind']] = cnt.get(r['ind'], 0) + 1
    wl[r['ind']] = r.get('wl')

ro = json.load(io.open('roster.json', encoding='utf-8'))
done = {v['ind'].upper(): k for k, v in ro.items()}
done.update({'AGROCHEMICALS': '001', 'REFRACTORIES': '070', 'GRAPHITE ELECTRODES': '071',
             'GRAPHITE & CARBON MATERIALS': '071', 'ALUMINIUM': '072', 'COPPER': '073',
             'ZINC & LEAD': '074', 'SPECIALTY ALLOYS': '075', 'NON-FERROUS METALS': '075',
             'PRECIOUS METALS': '075', 'DIVERSIFIED METALS': '075', 'METAL RECYCLING': '076',
             'METAL TRADING': '077', 'CASTINGS & FOUNDRIES': '078'})

def fam_of(p):
    n = int(p)
    for lo, hi, f in [(1, 16, 'Chemicals'), (17, 27, 'Auto'), (28, 35, 'Oil & Gas'),
                      (36, 48, 'Power & Energy'), (49, 49, 'Consumer'), (50, 56, 'Electronics & EMS'),
                      (57, 62, 'Defence'), (63, 63, 'Capital Markets'), (64, 77, 'Metals'),
                      (78, 999, 'Engineering & Capital Goods')]:
        if lo <= n <= hi:
            return f

M = 'Suggest merging into '
Q = [
 ('Metals - gap to close', False, [
    ('INDUSTRIAL MINERALS & MINING', 'Missed when Metals was marked complete; do this first.')]),
 ('Engineering & Capital Goods', False, [
    ('FORGINGS', ''), ('METAL FABRICATION & ENGINEERING', ''),
    ('FASTENERS', 'Suggest merging with Industrial Tools and Abrasives.'),
    ('INDUSTRIAL TOOLS', M + 'Fasteners.'), ('ABRASIVES', M + 'Fasteners.'),
    ('WELDING & CUTTING EQUIPMENT', ''), ('BEARINGS', ''),
    ('INDUSTRIAL GEARS & TRANSMISSION', 'Suggest merging with Hydraulics & Motion Control.'),
    ('HYDRAULICS & MOTION CONTROL', M + 'Industrial Gears.'),
    ('PUMPS', ''),
    ('VALVES', 'Suggest merging with Flexible Hoses & Piping.'),
    ('FLEXIBLE HOSES & PIPING SYSTEMS', M + 'Valves.'),
    ('COMPRESSORS', 'Suggest merging with Industrial Engines.'),
    ('INDUSTRIAL ENGINES', M + 'Compressors.'),
    ('MACHINE TOOLS', ''),
    ('INDUSTRIAL MACHINERY', 'Suggest absorbing Foundry & Metal Processing Equipment.'),
    ('FOUNDRY & METAL PROCESSING EQUIPMENT', M + 'Industrial Machinery.'),
    ('MATERIAL HANDLING EQUIPMENT', ''), ('CONSTRUCTION & MINING EQUIPMENT', ''),
    ('INDUSTRIAL AUTOMATION & INSTRUMENTATION', ''),
    ('HEAT EXCHANGERS & PROCESS EQUIPMENT', 'Suggest absorbing Cryogenic, Bioenergy & Distillery and Industrial Furnaces.'),
    ('CRYOGENIC EQUIPMENT', M + 'Heat Exchangers.'),
    ('BIOENERGY & DISTILLERY EQUIPMENT', M + 'Heat Exchangers.'),
    ('INDUSTRIAL FURNACES & HEATING', M + 'Heat Exchangers.'),
    ('GAS CYLINDERS & CONTAINERS', ''),
    ('POLLUTION CONTROL EQUIPMENT', 'Suggest merging with Industrial Filters.'),
    ('INDUSTRIAL FILTERS & SEPARATION', M + 'Pollution Control.'),
    ('INDUSTRIAL HVAC & REFRIGERATION', 'Suggest merging with Cleanroom & HVAC.'),
    ('CLEANROOM & HVAC ENGINEERING', M + 'Industrial HVAC.'),
    ('TEXTILE MACHINERY', 'Suggest merging with Plastic & Packaging and Food & Agri machinery.'),
    ('PLASTIC & PACKAGING MACHINERY', M + 'Textile Machinery.'),
    ('FOOD & AGRICULTURAL MACHINERY', M + 'Textile Machinery.'),
    ('INDUSTRIAL SAFETY PRODUCTS', ''), ('RAILWAY EQUIPMENT', ''),
    ('ENGINEERING R&D SERVICES', 'Suggest merging with Engineering Consultancy.'),
    ('ENGINEERING CONSULTANCY', M + 'Engineering R&D.')]),
 ('Electrical Equipment & Power - gaps', False, [
    ('ELECTRICAL EQUIPMENT', 'Power & Energy (036-048) was marked complete but missed these.'),
    ('ELECTRICAL EQUIPMENT REPAIR', M + 'Electrical Equipment.'),
    ('ELECTRIC MOTORS & GENERATORS', ''),
    ('ELECTRICAL INSULATORS & BUSHINGS', 'Suggest merging with Transformer Components.'),
    ('TRANSFORMER COMPONENTS', M + 'Insulators & Bushings; see 042.'),
    ('TRANSMISSION TOWERS & STRUCTURES', ''),
    ('WIND TURBINES & EQUIPMENT', 'Suggest merging with Renewable O&M.'),
    ('RENEWABLE O&M SERVICES', M + 'Wind Turbines.'),
    ('RENEWABLE ENERGY SOLUTIONS', ''),
    ('BIOFUELS & ETHANOL', 'Cross-reference Sugar & Integrated Ethanol later.')]),
 ('Construction & Building Materials', False, [
    ('CEMENT', ''), ('CONSTRUCTION & INFRASTRUCTURE EPC', '98 names - split sensibly by segment.'),
    ('ROAD CONSTRUCTION', ''), ('RAILWAY EPC', ''), ('WATER INFRASTRUCTURE & TREATMENT', ''),
    ('DREDGING', ''), ('GLASS', ''), ('TILES & SANITARYWARE', ''),
    ('PLYWOOD LAMINATES & BOARDS', ''), ('PLASTIC PIPES & FITTINGS', ''),
    ('STONE & OTHER BUILDING MATERIALS', ''),
    ('BUILDING HARDWARE', M + 'Stone & Other Building Materials.')]),
 ('Transport & Logistics', False, [
    ('RAIL LOGISTICS', ''), ('PORTS & TERMINALS', ''), ('SHIPPING OPERATORS', ''),
    ('CONTAINER & WAREHOUSE LOGISTICS', ''), ('FREIGHT FORWARDING & LOGISTICS', '63 names - heavy audit.'),
    ('EXPRESS & PARCEL LOGISTICS', ''), ('COLD CHAIN LOGISTICS', ''), ('AIRLINES', ''),
    ('AIRPORTS & AVIATION SERVICES', ''), ('VEHICLE RENTAL & MOBILITY SERVICES', '')]),
 ('Materials: Plastics, Rubber, Packaging & Paper', False, [
    ('CARBON BLACK', 'A chemicals gap (not in 001-016); tyre input, see 025 and 071.'),
    ('INDUSTRIAL PLASTICS & COMPOSITES', ''), ('INDUSTRIAL RUBBER PRODUCTS', ''),
    ('FLEXIBLE PACKAGING & FILMS', ''), ('RIGID PLASTIC PACKAGING', ''), ('METAL PACKAGING', ''),
    ('PACKAGING PRODUCTS', ''), ('PAPER & PAPERBOARD', ''), ('PRINTING SERVICES', '')]),
 ('Textiles', False, [
    ('COTTON & BLENDED YARN', '75 names - heavy audit.'), ('SYNTHETIC FIBRES & YARNS', ''),
    ('FABRICS & TEXTILE PROCESSING', ''), ('INTEGRATED TEXTILES', ''), ('HOME TEXTILES', ''),
    ('TECHNICAL TEXTILES', ''), ('APPAREL MANUFACTURING', ''), ('JUTE PRODUCTS', ''),
    ('LEATHER & LEATHER PRODUCTS', '')]),
 ('Technology & Telecom', False, [
    ('IT SERVICES & CONSULTING', '128 names - split sensibly.'), ('SOFTWARE PRODUCTS & PLATFORMS', ''),
    ('BPM & OUTSOURCING SERVICES', ''),
    ('BANKING & FINANCIAL SOFTWARE', 'Software, not financial services - not deferred.'),
    ('DATA ANALYTICS & AI SERVICES', ''), ('CYBERSECURITY', ''), ('CLOUD COMMUNICATIONS', ''),
    ('DATA CENTRES & CLOUD INFRASTRUCTURE', ''), ('GEOSPATIAL & MAPPING', ''),
    ('IT HARDWARE & DISTRIBUTION', ''), ('INTERNET PLATFORMS', ''), ('E-COMMERCE & INTERNET RETAIL', ''),
    ('FOOD DELIVERY & QUICK COMMERCE', ''), ('TELECOM OPERATORS', ''),
    ('TELECOM TOWERS & INFRASTRUCTURE', ''), ('TELECOM EQUIPMENT & OPTICAL FIBRE', '')]),
 ('Consumer', False, [
    ('CONSUMER APPLIANCES & ELECTRONICS', ''), ('LIGHTING & ELECTRICAL ACCESSORIES', ''),
    ('CONSUMER PRODUCTS', ''), ('CONSUMER CONTRACT MANUFACTURING', ''),
    ('PERSONAL CARE & HOUSEHOLD PRODUCTS', ''), ('FURNITURE & HOME PRODUCTS', ''),
    ('JEWELLERY RETAIL & MANUFACTURING', '70 names - heavy audit.'), ('WATCHES & ACCESSORIES', ''),
    ('EYEWEAR', ''), ('FOOTWEAR', ''), ('LUGGAGE & TRAVEL ACCESSORIES', ''), ('ELECTRONICS RETAIL', ''),
    ('RETAIL CHAINS', ''), ('STATIONERY & EDUCATION PRODUCTS', ''), ('TOYS & LEISURE PRODUCTS', ''),
    ('PERSONAL & HOME SERVICES', '')]),
 ('Food, Beverages & Agri', False, [
    ('SEEDS & AGRICULTURAL INPUTS', 'Cross-reference 001 and 014.'),
    ('AGRICULTURE & COMMODITY TRADING', ''), ('SUGAR & INTEGRATED ETHANOL', ''), ('EDIBLE OILS', ''),
    ('RICE & GRAIN PROCESSING', ''), ('TEA & COFFEE', ''), ('DAIRY', ''), ('POULTRY & ANIMAL FEED', ''),
    ('MEAT & POULTRY PROCESSING', ''), ('SEAFOOD & AQUACULTURE', ''),
    ('PACKAGED FOODS & FOOD PROCESSING', '88 names - heavy audit.'), ('GELATIN & FOOD INGREDIENTS', ''),
    ('NON-ALCOHOLIC BEVERAGES', ''), ('ALCOHOLIC BEVERAGES', ''), ('TOBACCO', '')]),
 ('Media, Services & Leisure', False, [
    ('ADVERTISING & MARKETING', ''), ('TV & RADIO BROADCASTING', ''), ('FILM MUSIC & CONTENT', ''),
    ('CINEMA EXHIBITION', ''), ('PUBLISHING & NEWS', ''), ('LEISURE & GAMING', ''),
    ('EVENTS & EXHIBITIONS', ''), ('RESTAURANTS & QSR', ''),
    ('TRAVEL & TOURISM', 'Adjacent to Hotels (deferred) but not itself deferred.'),
    ('RAILWAY CATERING & TOURISM', ''), ('EDUCATION & TRAINING', ''),
    ('PROFESSIONAL & BUSINESS SERVICES', ''), ('STAFFING & FACILITY MANAGEMENT', ''),
    ('TESTING INSPECTION & CERTIFICATION', ''), ('WASTE MANAGEMENT & RECYCLING', 'Cross-reference 076.')]),
 ('Real Estate & Infrastructure Assets', False, [
    ('REAL ESTATE DEVELOPMENT', '168 names - split sensibly.'), ('REAL ESTATE SERVICES', ''),
    ('REITS', ''), ('INFRASTRUCTURE INVESTMENT TRUSTS', ''), ('FLEXIBLE WORKSPACES', ''),
    ('ROAD ASSET OPERATORS', '')]),
 ('Diversified', False, [
    ('DIVERSIFIED BUSINESSES', ''), ('TRADING & DISTRIBUTION', 'Unrelated grab-bag; see the note in 077.')]),
 ('Financials & Capital Markets - LAST', True, [(s, '') for s in [
    'PRIVATE SECTOR BANKS', 'PUBLIC SECTOR BANKS', 'SMALL FINANCE BANKS', 'DIVERSIFIED & OTHER LENDING',
    'HOUSING FINANCE', 'VEHICLE FINANCE', 'GOLD FINANCE', 'MICROFINANCE', 'INFRASTRUCTURE FINANCE',
    'CREDIT CARDS', 'PAYMENTS & FINTECH', 'FOREIGN EXCHANGE & REMITTANCES', 'DIVERSIFIED FINANCIAL SERVICES',
    'INVESTMENT HOLDING COMPANIES', 'STOCKBROKING & INVESTMENT BANKING', 'ASSET MANAGEMENT',
    'WEALTH MANAGEMENT', 'REGISTRARS & FUND SERVICES', 'CREDIT RATING AGENCIES', 'FINANCIAL DATA & RESEARCH',
    'FINANCIAL PRODUCT DISTRIBUTION', 'TRUSTEESHIP & CORPORATE ADVISORY', 'EXCHANGE-TRADED FUNDS']]),
 ('Insurance - LAST', True, [(s, '') for s in [
    'LIFE INSURANCE', 'GENERAL INSURANCE', 'HEALTH INSURANCE', 'INSURANCE DISTRIBUTION']]),
 ('Pharma & Healthcare - LAST', True, [(s, '') for s in [
    'PHARMA FORMULATIONS', 'PHARMA APIS & INTERMEDIATES', 'PHARMA CONTRACT RESEARCH & MANUFACTURING',
    'PHARMA EXCIPIENTS', 'PHARMA DISTRIBUTION & RETAIL', 'BIOLOGICS & VACCINES', 'MEDICAL DEVICES & SUPPLIES',
    'DIAGNOSTICS', 'HOSPITALS', 'HEALTHCARE ADMINISTRATION SERVICES']] +
    [('NUTRACEUTICALS & CONSUMER HEALTH', 'Borderline consumer/health; held back with healthcare to respect the instruction.')]),
 ('Hotels - LAST', True, [('HOTELS & RESORTS', '')]),
]

out = []; seen = set(); order = 0
for s, n in cnt.items():
    if s.upper() in done:
        p = done[s.upper()]
        out.append(dict(section=s, watchlist=wl[s], members=n, status='done', primer=p,
                        family=fam_of(p), order=None, note=''))
        seen.add(s)
for fam, defer, items in Q:
    for s, note in items:
        assert s in cnt, 'unknown section ' + s
        assert s not in seen, 'duplicate ' + s
        order += 1
        out.append(dict(section=s, watchlist=wl[s], members=cnt[s],
                        status='deferred' if defer else 'queued', primer=None, family=fam,
                        order=order, note=note))
        seen.add(s)
missing = [s for s in cnt if s not in seen]
assert not missing, missing
assert len(out) == 278, len(out)
json.dump(out, io.open('sections.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('sections.json written:', dict(collections.Counter(x['status'] for x in out)))
