#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 'qwer'
b = 55


def typer(incom):
	a = type(incom)
	a = str(a)
	in_list = a.split("'")
	return in_list[1]

print 'typer(', a, ') == ', typer(a)
print 'typer(', b, ') == ', typer(b)
print 'typer(typer) == ', typer(typer)


