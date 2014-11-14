#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 1: Квадраты " + "_"*15
l = [1, 2, 3, 4]
t = (5, 6, 7, 8)
print "L = ", l
print "T = ", t

# ==============================
print "variant 1:"

l1 = [x**2 for x in l]
print "  Result: L1 >>> ", l1

t1 = tuple(x**2 for x in t)
print "  Result: T1 >>> ", t1


# ===============================
print "variant 2:"

def power(x, y=2):
    return x**y

l2 = map(power, l)
print "  Result: L2 >>> ", l2

t2 = tuple(map(lambda x: x**2, t))
print "  Result: T2 >>> ", t2
