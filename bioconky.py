#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Show biorhythm warnings like the KOSMOS-1 calculator with Conky
P: physical
E: emotional
I: intellectual

2013-08-26

Red: critical days
Orange: mini-critical days
See http://decodesystems.com/kosmos-1.html

The dominant cycle for each day is shown in parentheses.

argument 1: Skip x days ahead (0 = today). Useful to output the next several days in Conky;
                 just call bioconky several times with offsets 0,1,2,3,...


Sample usage in .conkyrc for the current day and a four-day forecast:

${font Monospace:size=11}PEI: ${execpi 100 python /home/username/bin/bioconky.py 0}
${alignr}${font Monospace:size=11}+1d: ${execpi 100 python /home/username/bin/bioconky.py 1}
${alignr}${font Monospace:size=11}+2d: ${execpi 100 python /home/username/bin/bioconky.py 2}
${alignr}${font Monospace:size=11}+3d: ${execpi 100 python /home/username/bin/bioconky.py 3}
${alignr}${font Monospace:size=11}+4d: ${execpi 100 python /home/username/bin/bioconky.py 4}
"""

dd,mm,yy=1,1,1990

from datetime import date
from sys import argv
from math import sin,pi

t0 = date(yy,mm,dd).toordinal()
t1 = date.today().toordinal()

wa=(
((1,12,13),(7,18)),
((1,15),(8,22)),
((1,17,18),(9,26))
)

s = {'_': '${color green}●${color}', 'y': '${color yellow}●${color}', 'r': '${color red}●${color}'}

out = ''

try:
    dt = int(argv[1])
except:
    dt = 0
t = t1 + dt

w = ['_','_','_']
o = ['*','*','*']
perc = [0,0,0]
for c in range(3):
    p = 23+5*c
    perc[c] = 100.*sin(2*pi*(t-t0)/p)
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

if perc[0]>perc[1] and perc[0]>perc[2]:
    out += '(P)'
elif perc[1]>perc[0] and perc[1]>perc[2]:
    out += '(E)'
else:
    out += '(I)'

print(out)
