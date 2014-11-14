#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 7
# 
print '----------------------------------------------------'

input_list=[1,4,8,6,3,7,1]


print 'INPUT: ', input_list
print '===================='

result = input_list
result.sort()

for n, m in enumerate(result):
	if m%2 != 0:
		result.remove(m)
		result.insert(0, m)

i=0
for n, m in enumerate(result):
	if m%2 == 0:
		result.remove(m)
		result.insert(i, m)
		i+=1

result.reverse()

print 'result: ', result
print '-----------------------------------------------------'
print 'check [1,4,8,6,3,7,1] is [1,1,3,7,8,6,4]'
if input_list is result:
	print 'OK'

   
print '-----------------------------------------------------'