# -*- coding: utf-8 -*-
__author__ = 'm_shalamov'


def func(A, B):
    if type(A) is str or type(B) is str:
        print u'"получена строка"'
    elif A > B:
        print u'"больше"'
    elif A == B:
        print u'"равны"'
    elif A < B:
        print u'"меньше"'

if __name__ == '__main__':
    func(1, "")
    func(1, 0)
    func(1, 1)
    func(1, 2)