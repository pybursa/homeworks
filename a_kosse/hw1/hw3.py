#!/usr/bin/env python
# -*- coding: utf-8 -*-

#in_string = raw_input('Input string:')
in_string = 'wowhatamanwowowpalehche'
low_string = in_string.lower()
counts = 0
for i in range(len(in_string)-2):
	if low_string[i:i+3] == 'wow':
		counts +=1

print 'Result:', counts
