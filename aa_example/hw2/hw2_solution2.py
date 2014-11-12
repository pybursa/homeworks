# -*- coding: utf8 -*-

u"""
Решение задачи#2 ДЗ#2 - Симметрия.

УСЛОВИЕ:
Фрагмент кода, который принимает строку и определяет симметрична ли строка.
(Возвращает True или False).

Пример:
"abba" >> True
"arbat" >> False
"""

__author__ = "a_kosse"
__email__ = "kosse@mail.me"
__date__ = "2014-11-12"


def symmetry_1(string):
    u"""Решение через срезы"""
    return string == string[::-1]


def symmetry_2(string):
    u"""Итеративное решение сравнением пар первого и последнего символа"""
    while len(string) > 1:
        if string[0] != string[-1]:
            return False
        string = string[1:-1]
    return True
