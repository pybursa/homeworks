#!/usr/bin/python
# -*- coding: utf-8 -*-
from types import *
def typer(x,y):
	if type(x) is StringType or type(y) is StringType :
		print u'получена строка'
	else:
		if x > y:
			print u'больше'
		elif x < y:
			print u'меньше'
		else:
			print u'равно'
typer("12", 4)
typer("12","4")
typer(12, 4)
typer(4, 45)
typer(4, 4)