#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 3. 8
# импорт модулей sys, os описание модулей:

import os
import sys

print 'if you need "DIR OS" dial: 1'
print 'if you need "Help OS" dial: 2'
print 'if you need "DIR SYS" dial: 3'
print 'if you need "Help SYS" dial: 4'



while True:
	x = raw_input('make your choice: ')
	if x.isdigit():
		x = int(x)

		if x == 1:
			print dir(os)
			break
		elif x == 2:
			help(os)
			break
		elif x == 3:
			print dir(sys)
			break
		elif x == 4:
			help(sys)
			break
		else:
			print 'Please sellect from 1,2,3,4'

	else:
		print 'Please enter the number'

