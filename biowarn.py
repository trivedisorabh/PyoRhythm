"""
Show biorhythm warnings like the KOSMOS-1 calculator
P: physical
E: emotional
I: intellectual

2011-09-09

Red: critical days
Orange: mini-critical days
See http://decodesystems.com/kosmos-1.html

"""

dd,mm,yy=1,1,1990

ti ="P-E-I critical and mini-critical days for %04u-%02u-%02u" % (yy,mm,dd)

from datetime import date

t0 = date(yy,mm,dd).toordinal()
t1 = date.today().toordinal()

wa=(
((1,12,13),(7,18)),
((1,15),(8,22)),
((1,17,18),(9,26))
)

tag = ('Mo.','Di.','Mi.','Do.','Fr.','Sa.','So.')

s = {'_': '<font color="#00ff00">&#9679;</font>', 'y': '<font color="#ffd700">&#9679;</font>', 'r': '<font color="#ff0000">&#9679;</font>'}

print "<html><head><title>%s</title><body><h3>%s</h3>" % (ti, ti)

print '<font face="Courier New">'

for t in range(t1-3,t1+35):
	if not (date.fromordinal(t).day-1)%5 and (date.fromordinal(t).day-1)%30:
		print '<hr width="42%" align="left">'
	if date.fromordinal(t).day == 1:
		print '<hr width="60%" align="left">'
	w = ['_','_','_']
	o = ['*','*','*']
	for c in range(3):
		p = 23+5*c
		v = ((t-t0) % p)+1
		if (v-1) <= p/2:
			o[c] = 'H'
		if (v-1) >= p/2:
			o[c] = 'T'
		if v in wa[c][0]:
			w[c] = 'r'
			o[c] = 'K'
		if v in wa[c][1]:
			w[c] = 'y'
	a = date.fromordinal(t)
	print tag[a.weekday()], a
	for x in w:
		print s[x]
	for x in o:
		print x,
	print "<br>"

print "</font></body></html>"

