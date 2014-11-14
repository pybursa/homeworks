#!/usr/bin/env python
# -*- coding: utf-8 -*-

answer = 'yes'

while answer == 'yes':
	in_string = raw_input('Please, enter your string: ')
	low_string = in_string.lower()
	count = 0
	for i in low_string:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
			count += 1
	print 'The string contains ', count, ' vowels'
	answer = raw_input ('Continue? (yes/no) ')
	while (answer != 'no') and (answer != 'yes'):
		answer = raw_input ('Please, enter corrent answer. Continue? (yes/no) ')

