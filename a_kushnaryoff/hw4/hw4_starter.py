#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#4.

"""

__author__ = "a_kushnaryoff"
__date__ = "2014-11-14"


import hw4_solution1
import hw4_solution2
from hw4_tests import tests_for_hw4_solution1, tests_for_hw4_solution2


INPUT_1 = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta." \
          " Donec rutrum congue leo eget malesuada."  # input variant  for solution1 functions
INPUT_2_TEXT = """Proin eget tortor risus. \
Cras ultricies ligula sed magna dictum porta.
Donec rutrum congue leo eget malesuada."""  # input for solution2 functions


def runner():
    u"""Запускает выполнение всех задач
    """
    print INPUT_1, ">>\n", hw4_solution1.letters_fq(INPUT_1)
    print "=" * 80

    print INPUT_2_TEXT, ">>\n", hw4_solution2.string_cut(INPUT_2_TEXT)
    print INPUT_2_TEXT, ">>\n", hw4_solution2.string_cut(INPUT_2_TEXT, 10)
    print INPUT_2_TEXT, ">>\n", hw4_solution2.string_cut(INPUT_2_TEXT, 13)


if __name__ == '__main__':
    runner()
    tests_for_hw4_solution1()
    tests_for_hw4_solution2()
