#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 8
# 
print '----------------------------------------------------'

input_list=(1,4,8,6,3,7,1)

result=[]
step=[]

print 'INPUT: ', input_list
print '==========='
if len(input_list)%2 != 0:
	odd = 1
else:
	odd = 0

for n, m in enumerate(input_list):
	if n%2 == 0:
		step.append(m)
		if odd == 1 and n == len(input_list)-1:
			partly = tuple(step)
			result.append(partly)

	if n%2 != 0:
		step.append(m)
		partly = tuple(step)
		result.append(partly)
		step = []
 
result=tuple(result)       
print result	
   
print '-----------------------------------------------------'