import io
p='frag_055.html'; s=io.open(p,encoding='utf-8').read()
a='<div class="box pm"><span class="tag">The honest read</span><p>Genus is executing'
assert s.count(a)==1
add = """<h3>What comes after RDSS</h3>
  <p>A natural question is what happens when the programme ends. Three sources of demand outlast it. First, meters have finite lives, so the tens of crores being installed now will need replacing in the 2030s. Second, the AMISP contracts themselves run for 7–10 years, so the service income continues well after installation stops. Third, the data from smart meters enables new services — time-of-day tariffs, rooftop-solar net metering, outage management and theft analytics — that utilities may pay for. The risk is a gap between the end of the installation wave and the start of replacement, which is why the long-dated service revenue matters so much to the durability of the business.</p>
  """
s=s.replace(a, add+a)
io.open(p,'w',encoding='utf-8').write(s)
print('ok')
