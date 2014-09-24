#!/usr/bin/env python

import GeoIP

gasn=GeoIP.open("/usr/share/GeoIP/GeoIPASNum.dat", GeoIP.GEOIP_MEMORY_CACHE)                                                                                
gacc=GeoIP.open("/usr/share/GeoIP/GeoIP.dat", GeoIP.GEOIP_MEMORY_CACHE)

import os,sys
import re

reip=re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

def map_if_ip(ip):
    if reip.match(ip):
	return '%s,%.20s: %s' % (gacc.country_name_by_addr(ip), gasn.org_by_addr(ip), ip)
    return ip


line=sys.stdin.readline()
while line:
    n=map(map_if_ip, line.rstrip().split(' '))

    print ' '.join(n)
    line=sys.stdin.readline()

