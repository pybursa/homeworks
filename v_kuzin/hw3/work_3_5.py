#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 3. 5
# 

a = raw_input('введите цифры для суммирования: ')

count = []

for i in a:
	m = int(i)
	for n in range(0, m):
		count.append(1)
		
print 'сумма= ', len(count)
