#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 3
# 
print '----------------------------------------------------'

b={}
input_list=[3,7,12]

print 'INPUT: ', input_list

for i in input_list:
	if (i)%3 != 0:
		result = 0
	else:
		result = 1

	b[i]=bool(result)

print b 
   
print '-----------------------------------------------------'