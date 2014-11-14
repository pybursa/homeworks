#!/usr/bin/python
# -*- coding: utf-8 -*-
from types import *
b = ""
def typer(x):
	if type(x) is IntType:
		b = "int"
		print b
	elif type(x) is StringType:
		b = "str"
		print  b
	elif type(x) is FunctionType:
		b = "function"
		print  b

typer(666)
typer("666")
typer(typer)


