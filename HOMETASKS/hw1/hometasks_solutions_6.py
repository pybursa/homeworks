#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 6: А & B.
A = '4'
B = 2

if type(A) == str or type(B) == str:
    print "получена строка"
elif A > B:
    print "больше"
elif A == B:
    print "равны"
else:
    print "меньше"


if __name__ == "__main__":
    print "Ok!"
