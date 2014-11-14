#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 6
# 
print '----------------------------------------------------'

input_list={'a': 1, 3: [1,5], 'e': 'abc', '6': []} 

n_list = 0
n_str = 0
n_int = 0

result = {}.fromkeys(['list', 'str','int'], 0)		

print 'INPUT: ', input_list
print '==========='

for i in input_list.values():
	if type(i) is list:
		n_list +=1
				   
	if type(i) is str:
		n_str +=1
		
	if type(i) is int:
		n_int +=1

l_list = {}.fromkeys(['list'], n_list)	
l_str = {}.fromkeys(['str'], n_str)	
l_int = {}.fromkeys(['int'], n_int)
		
result.update(l_list)
result.update(l_str)
result.update(l_int)

print result

print '-----------------------------------------------------'