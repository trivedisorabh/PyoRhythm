#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Show biorhythm warnings like the KOSMOS-1 calculator with Conky
P: physical
E: emotional
I: intellectual

2013-01-02

Red: critical days
Orange: mini-critical days
See http://decodesystems.com/kosmos-1.html

"""

dd,mm,yy=1,1,1990

from datetime import date

t0 = date(yy,mm,dd).toordinal()
t1 = date.today().toordinal()

wa=(
((1,12,13),(7,18)),
((1,15),(8,22)),
((1,17,18),(9,26))
)

s = {'_': '${color green}●${color}', 'y': '${color yellow}●${color}', 'r': '${color red}●${color}'}

out = ""

for t in range(t1,t1+1):
	w = ['_','_','_']
	o = ['*','*','*']
	for c in range(3):
		p = 23+5*c
		v = ((t-t0) % p)+1
		if (v-1) <= p/2:
			o[c] = 'H'
		if (v-1) >= p/2:
			o[c] = 'L'
		if v in wa[c][0]:
			w[c] = 'r'
			o[c] = 'C'
		if v in wa[c][1]:
			w[c] = 'y'
	for x in w:
		out += s[x] + ' '
	for x in o:
		out += x + ' '

print(out)
