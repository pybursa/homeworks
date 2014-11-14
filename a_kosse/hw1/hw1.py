#!/usr/bin/env python
# -*- coding: utf-8 -*-

#in_string = raw_input('Input string:')
in_string = 'ambulance'
in_list = list(in_string)
in_list.reverse()

out_string1 = ''
for i in in_list:
	out_string1 += i
print out_string1

out_string2 = ''
for i in in_string:
	out_string2 = i + out_string2
print out_string2

out_string3 = ''
for i in range(len(in_string)-1,-1,-1):
	out_string3 += in_string[i]
print out_string3

out_string4 = in_string[::-1]
print out_string4