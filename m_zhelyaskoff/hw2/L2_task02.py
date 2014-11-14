#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 2: Симметрия " + "_"*15

s1 = "abba"
s2 = "arbat"
s3 = "radar"

def is_symmetrical(str):
    if str[::-1] == str: return True
    return False

print s1, " >>> ", is_symmetrical(s1)
print s2, " >>> ", is_symmetrical(s2)
print s3, " >>> ", is_symmetrical(s3)
