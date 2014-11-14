#!/usr/bin/python
# -*- coding: utf-8 -*-

print "\n\n___ Задание 4: Чет-нечет " + "_"*15
a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6, 7]
print "L1 = ", a
print "L2 = ", b


# ==================================================
print "variant 1:"
f1 = filter((lambda x: x % 2 == len(a)%2), a)
print "  Result L1 >>>", f1

f2 = filter((lambda x: x % 2 == len(b)%2), b)
print "  Result L2 >>>", f2, "\n"


# ==================================================
print "variant 2:"
f1 = [x for x in a if x % 2 == len(a)%2]
print "  Result L1 >>>", f1

f2 = [x for x in b if x % 2 == len(b)%2]
print "  Result L2 >>>", f2, "\n"


# ==================================================
print "variant 3:"
def even_odd(l):
    d = len(l)%2
    # return filter(lambda x: x%2==d, l)
    return [x for x in l if x%2==d]

f1 = even_odd(a)
print "  Result L1 >>>", f1

f2 = even_odd(b)
print "  Result L2 >>>", f2
