#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')

func1 = lambda t: t[2::3]

def func2(t_in):
	t_out = ()
	for i in range(2,len(t_in),3):
		t_out += t_in[i:i+1]
	return t_out



print func1(t)
print func2(t)
