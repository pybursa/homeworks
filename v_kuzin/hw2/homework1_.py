#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 1
#b= (1,2,3) or [1,2,3]

print '--------------------------------------------'
b=[1,2,3]
print 'input: ', b
d=[]

for i in b:
	c=i**2
	d.append(c)

if tuple is type(b):    #list --> tuple
	d=tuple(d)

print 'output: ', d
print '--------------------------------------------'
