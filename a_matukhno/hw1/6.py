# -*- coding: utf-8 -*-

a = 123
b = 123


def analyze(a, b):
    pass
    if isinstance(a, type('')) or isinstance(b, type('')):
        print 'получена строка'
    elif a > b:
        print 'больше'
    elif a == b:
        print 'равны'
    elif a < b:
        print 'меньше'

analyze(a, b)