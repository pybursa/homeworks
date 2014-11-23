#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ№4.

Данный скрипт призван запускать на выполнение домашнее задание №4
путём импортирования решений из соответствующих модулей. Также
выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = 'Viktorov Eugene'
__email__ = 'jekafromua@gmail.com'
__date__ = '2014-11-16'


import hw4_solution_1
import hw4_solution_2


INPUT_1 = 'Proin eget tortor risus. \
Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada.'

INPUT_2 = 'Proin eget tortor risus. \
Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada.'

INPUT_2_1 = 4
INPUT_2_2 = 10
INPUT_2_3 = 27


def runner():
    print INPUT_1, ">>\n", hw4_solution_1.percent(INPUT_1)

    print INPUT_2, ">>\n>>", hw4_solution_2.limitation(INPUT_2, INPUT_2_1)
    print '...', ">>", hw4_solution_2.limitation(INPUT_2, INPUT_2_2)
    print '...', ">>", hw4_solution_2.limitation(INPUT_2, INPUT_2_3)


if __name__ == '__main__':
    runner()
