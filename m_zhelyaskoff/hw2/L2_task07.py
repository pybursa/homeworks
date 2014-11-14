#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 7: Сепаратор.Адвансед " + "_"*15

# ===============================================
l = [1,4,8,6,3,7,1]
print "L = ", l

print "variant 1"
l.sort()
l.sort(key=lambda x: x%2, reverse=True)

print "  Result L1 >>> ", l, "\n"


# ===============================================
print "variant 2"
l = [1,4,8,6,3,7,1]
l.sort()
p = i = len(l)-1
while  i >= 0:
    if l[i] % 2 == 0:
        l.insert(p, l.pop(i))
        p -= 1
    i -= 1

print "  Result L2 >>> ", l, "\n"


# ===============================================
print "variant 3"
l = [1,4,8,6,3,7,1]
l.sort()
for x in l[:]:
    if x % 2 == 0:
        l.remove(x)
        l.append(x)

print "  Result L3 >>> ", l
