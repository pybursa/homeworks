#!/usr/bin/python
# -*- coding: utf-8 -*-
s = "hApPyHalLOweEn!"
a = "aeiou"
s = s.lower()
b = 0
for char in s:
	b += a.count(char)
print b