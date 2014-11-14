#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 4
# 
print '----------------------------------------------------'


input_list=[3,7,12,7]
result=[]

if len(input_list)%2 != 0:
	ip = 1                     #odd-
else:
	ip = 0                     #even

print 'INPUT: ', input_list
print '==========='
for i in input_list:
	if (i)%2 != 0 and ip == 1:  #odd
		result.append(i)
	if (i)%2 == 0 and ip == 0:  #even
		result.append(i)

	
print result
   
print '-----------------------------------------------------'