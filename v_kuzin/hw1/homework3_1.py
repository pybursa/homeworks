#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3
# ? - wow
print '*****************************************'
s = "wowhatamanwowowpalehche"
print 'INPUT'
print s
print '"wow -?"'
l=len(s)           #length
control_word='wow'
result=0

for i in xrange(0,l):
    word=s[i-2]+s[i-1]+s[i]
    if word==control_word:
        result+=1

print '-----------------------------------------'
print 'result=',result
print '*****************************************'
