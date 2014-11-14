#!/usr/bin/env python
# -*- coding: utf-8 -*-

def comparison(A, B):
	str_type = type('')
	if type(A) == str_type or type(B) == str_type:
		print u"получена строка"
	elif A > B:
		print u"больше"
	elif A == B:
		print u"равно"
	elif A < B:
		print u"меньше"
	return None

comparison('q',1)
comparison(1,1)
comparison(2,1)
comparison(-1,1)