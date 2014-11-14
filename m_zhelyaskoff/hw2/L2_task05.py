#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 5: Сепаратор " + "_"*15

a = [1, 14, 8, 5, 7, 11, 4, 9, 16, 1]
print "List = ", a

def even_odd_sort(l):
    l.sort()
    l1 = [x for x in l if x%2==1]
    l2 = [x for x in l if x%2==0]
    return l1+l2

res = even_odd_sort(a)
print "  Result = ", res
