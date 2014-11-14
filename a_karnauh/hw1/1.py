#!/usr/bin/python
# -*- coding: utf-8 -*-
#1-st variant
string = "ecnalubma"
array = list(string)
array.reverse()
print "Result 1:", "".join(array)

#2-nd variant
print "Result 2:", string[ : : -1]

#3-d variant
result3 = ""
for i in range(len(string)-1, -1, -1):
	result3 += string[i]
print "Result 3:", result3

#4 variant
result4 = ""
for char in string:
	result4 = char + result4
print "Result 4:", result4