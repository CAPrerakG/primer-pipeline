import io
p='frag_055.html'; s=io.open(p,encoding='utf-8').read()
a='<h3>Leadership shifts, and what caused them</h3>'
assert s.count(a)==1
add = """<p>India's choice of the AMISP model was deliberate. Many discoms could not fund a national meter replacement from their own balance sheets, and earlier meter-purchase programmes often ended with meters installed but systems poorly maintained. Paying a private provider a monthly fee tied to performance shifts both the financing and the operating responsibility, in exchange for a long-term claim on discom cash flows. Whether that bargain works depends on discoms honouring payments — the same question that has shaped every earlier reform of India's power distribution.</p>
  """
s=s.replace(a, add+a)
io.open(p,'w',encoding='utf-8').write(s)
print('ok')
