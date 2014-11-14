#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 3: Триделение " + "_"*15

l = [3, 7, 12, 4, 9]
print "L = ", l

# ==================================================
print "variant 1"
d1 = dict.fromkeys(l)
for key in d1.keys():
    d1[key] = not bool(key % 3)
print "  Result D1 >>>", d1, "\n"

# ==================================================
print "variant 2"
d2 = {x: bool(x % 3 == 0) for x in l}
print "  Result D2 >>>", d2
