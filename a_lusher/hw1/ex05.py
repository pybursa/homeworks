#!usr/bin/python

import types

#my_string=raw_input("Please enter a string: ")

def typer(my_string):
	if my_string==typer:
		return "function"
	if my_string<>"typer":	
		return str(type(my_string))[7:][:3]

print typer(666)
print typer("666")
print typer(typer)
