# -*- coding: utf8 -*-

u"""
Решение задачи#1 ДЗ#2 - Квадраты.

УСЛОВИЕ:
Фрагмент кода, который принимает набор (список, кортеж) чисел и возвращает набор
ТОГО ЖЕ типа со значениями квадратов этих чисел.

Пример:
[1,2,3] >> [1,4,9]
(1,2,3) >> (1,4,9)
"""

__author__ = "a_kosse"
__email__ = "kosse@mail.me"
__date__ = "2014-11-12"


def squares_1(L):
    u"""Решение через простые итерации."""
    assert type(L) in [tuple, list]
    type_name = type(L)
    result = []
    for item in L:
        result.append(item * item)
    return type_name(result)


def squares_2(L):
    u"""Решение с использованием генератора списков."""
    type_name = type(L)
    return type_name([item ** 2 for item in L])


def squares_3(L):
    u"""Решение с использованием встроенной функции map()."""
    return type(L)(map(lambda x: x**2, L))
