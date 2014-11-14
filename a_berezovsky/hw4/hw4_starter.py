#!/usr/bin/env python2
# coding=utf-8
"""
Starting file for PyBursa HW4
"""
from hw4_solution1 import task01
from hw4_solution2 import task02

if __name__ == '__main__':
    text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. " \
           "Donec rutrum congue leo eget malesuada."
    print task01(text)
    print task01("ABCda")
    text = "Proin eget tortor risus."
    print task02(text, 24)
    print task02(text, 23)
    print task02(text, 13)
    print task02(text, 6)

