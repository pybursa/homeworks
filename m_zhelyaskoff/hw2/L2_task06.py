#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 6: Классификатор " + "_"*15
d = {'a': 1, 3: [1, 5], 'e': 'abc', '6': []}
print "Dict = ", d


# ==================================================
print "variant 1"
types = [type(x).__name__ for x in d.values()]
res_1 = dict((x, types.count(x))  for x in set(types))
print "  Result = ", res_1, "\n"


# ==================================================
print "variant 2"
res_2 = {}
for x in d.values():
    key = type(x).__name__
    if res_2.has_key(key):
        res_2[key] = res_2[key] + 1
    else:
        res_2[key] = 1

print "  Result = ", res_2





