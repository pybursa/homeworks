#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 8: Двууровневый кортеж " + "_"*15

t = (1,4,8,6,3,7,1)
print "start_typle = ", t


print "variant 1"
res1 = tuple(map(None, t[0::2], t[1::2]))
print "  end_tuple = ", res1, "\n"


print "variant 2"
res2 = zip(t[0::2], t[1::2])
if len(t) % 2 != 0:
    res2.append((t[-1],))
res2 = tuple(res2)
print "  end_tuple = ", res2
