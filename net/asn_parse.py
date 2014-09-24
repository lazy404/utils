#!/usr/bin/env python


import os,sys
import re

reip=re.compile(r'^\d{1,6}$')

def map_if_as(a):
    if reip.match(a):
        asn='AS%s' % a
	return 'AS%s:%.40s' % (a, db.get(asn, asn))
    return a

f=open('/usr/lib/asndb.txt', 'r')
ln=map(lambda x: x.rstrip('\n'), f.readlines())
f.close()

db={}
for t in map(lambda x: x.split(' ', 1), ln):
    if len(t) == 2:
        db[t[0]]=t[1]

line=sys.stdin.readline()
while line:

    n=map(map_if_as, line.rstrip().split(' '))

    print ' '.join(n)
    line=sys.stdin.readline()

