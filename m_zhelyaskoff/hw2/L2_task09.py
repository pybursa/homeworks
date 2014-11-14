#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 9: Уплощение строптивого " + "_"*15

l = [[1],[4,8],[6,3,7],[1,3]]
print "start_list = ", l

res = [y for x in l for y in x]
print "  end_list = ", res
