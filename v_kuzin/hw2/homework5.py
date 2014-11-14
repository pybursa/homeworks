#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 5
# 
print '----------------------------------------------------'


input_list=[1,4,8,6,3,7,1]
result_odd=[]
result_even=[]
result=[]


print 'INPUT: ', input_list
print '==========='
for i in input_list:
	if (i)%2 != 0:                 #odd              
		result_odd.append(i)       
	else:                          #even
		result_even.append(i)
		

result_odd.sort()
result_even.sort()

result = result_odd  + result_even[::-1]
print  result
   
print '-----------------------------------------------------'