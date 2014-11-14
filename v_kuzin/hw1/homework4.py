#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4
# ? - wow
print '*****************************************'
s = "sabrrtuwacaddabra"
print 'INPUT'
print s

l=len(s)           #length
str_if=[]
word=[]

for i in xrange(0,l):
    word=s[i]
    for n in xrange(i+1,l):
        if s[n-1]<=s[n]:
            word=word+s[n]
        else:
            str_if.append(word)
            break

print '-----------------------------------------'

print 'result=',str_if

print '*****************************************'
