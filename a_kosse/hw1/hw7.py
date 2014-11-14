#!/usr/bin/env python
# -*- coding: utf-8 -*-

def unique_ordered(in_list):
	out_list = []
	for i in in_list:
		if not i in out_list:
			out_list.append(i)
	return out_list

print unique_ordered(["a", 5, 2, 5, (1, "a"), "a"])