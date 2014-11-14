#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Задание 6: Простые числа. (бонусное)
#
# УСЛОВИЕ:
# Вывести на печать 10000 первых натуральных простых чисел.
# Напомню, что это те, которые делятся без остатка не себя и 1, начиная с числа 2.
__author__ = 'maln'


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

i = 1;
count_of_prime = 0
while count_of_prime < 10000:
    if isprime(i):
        print i
        count_of_prime += 1
    i += 1
