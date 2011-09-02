"""
Show biorhythm warnings like the KOSMOS-1 calculator
P: physical
E: emotional
I: intellectual

2011-09-02

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

s = {'_': '<font color="#cccccc">&#9679;</font>', 'y': '<font color="#ffd700">&#9679;</font>', 'r': '<font color="#ff0000">&#9679;</font>'}

print "<html><head><title>%s</title><body><h2>%s</h2>" % (ti, ti)

print '<font face="Courier New">'

for t in range(t1-3,t1+41):
	w = ['_','_','_']
	for c in range(3):
		p = 23+5*c
		v = ((t-t0) % p)+1
		if v in wa[c][0]:
			w[c] = 'r'
		if v in wa[c][1]:
			w[c] = 'y'
	print date.fromordinal(t)
	for x in w:
		print s[x]
	print "<br>"

print "</font></body></html>"

