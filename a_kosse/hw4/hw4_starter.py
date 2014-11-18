#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#4.

Данный скрипт призван запускать на выполнение домашнее задание #4 путем
импортирования решений из соответствующих модулей. Также выполняется комплекс
тестов из модуля набора тестов.
"""

__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-15"
__license__ = "GPL"
__version__ = "0.0.1"



import hw4_solutions1
import hw4_solutions2
from hw4_test import (tests_for_hw4_solution1, tests_for_hw4_solution2)


INPUT_TEXT = """Proin eget tortor risus. Cras ultricies ligula sed magna \
dictum porta. Donec rutrum congue leo eget malesuada."""
INPUT_2_limit = 14     # input variant B for solution2 functions


def runner():
    u"""Запускает выполнение всех задач"""
    print INPUT_TEXT, ">>", hw4_solutions1.freq_letter(INPUT_TEXT)
    print
    print INPUT_TEXT, "; limit = ", INPUT_2_limit, ">>",
    print hw4_solutions2.afterword(INPUT_TEXT, INPUT_2_limit)


if __name__ == '__main__':
    runner()
    tests_for_hw4_solution1()
    tests_for_hw4_solution2(INPUT_TEXT)
