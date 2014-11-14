#!/usr/bin/env python
# -*- coding: utf-8 -*-


#in_string = raw_input('Input string:')
in_string = 'hApPyHalLOweEn!'
low_string = in_string.lower()
count = 0
for i in low_string:
	if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
		count += 1

print 'Result: ', count
