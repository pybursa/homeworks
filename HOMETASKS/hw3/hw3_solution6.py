#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание 6: Простые числа. (бонусное)

УСЛОВИЕ:
Вывести на печать 10000 первых натуральных простых чисел.
Напомню, что это те, которые делятся без остатка не себя и 1, начиная с числа 2.
"""

__author__ = 'wowkalucky'


def simples_gen():
    n = 1
    current = 2
    print current
    while n < 10000:
        current += 1
        for i in range(2, current):
            if current % i == 0:
                break
        else:
            n += 1
            print current


if __name__ == "__main__":
    simples_gen()
