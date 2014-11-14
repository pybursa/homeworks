#!/usr/bin/python
# -*- coding: utf-8 -*-
s = "sabrrtuwacaddabra"
count_max = 0
count = 0
pos = 0
for i in range(0, len(s)-1, 1):
	if s[i]<=s[i+1]:
		count += 1
	else:
		if count_max < count:
			count_max = count
			pos = i - count
		count = 0

print s[pos:pos+count_max+1:1]