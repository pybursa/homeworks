#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 2
# 
print '*****************************************'

print "Please, enter your string: "
s=raw_input()

a=list(s)
a.reverse()

if s in "".join(a):
	print 'True'
else:
	print 'False'
print '*****************************************'