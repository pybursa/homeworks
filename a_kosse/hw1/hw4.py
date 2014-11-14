#!/usr/bin/env python
# -*- coding: utf-8 -*-

#in_string = raw_input('Input string:')
in_string = 'sabrrtuwacaddabra'
low_string = in_string.lower()
number, count,count_temp = 0, 1, 1
for i in range(1,len(low_string)):
	if low_string[i-1] <= low_string[i]:
		count_temp += 1
	else:
		if count_temp > count:
			number = i - count_temp
			count = count_temp
		count_temp = 1
		
if count_temp > count:
	count = count_temp
	
print 'Result:', low_string[number:(number + count)]