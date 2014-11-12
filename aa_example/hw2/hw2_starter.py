#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#2.

Данный скрипт призван запускать на выполнение домашнее задание #2 путем импортирования решений из соответствующих
модулей. Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = "a_kosse"
__email__ = "kosse@mail.me"
__date__ = "2014-11-12"


import hw2_solution1
import hw2_solution2
from hw2_tests import (tests_for_hw2_solution1, tests_for_hw2_solution2,
                       tests_for_hw2_solution3)


INPUT_1 = [1, 2, 3]     # input for solution1 functions
INPUT_2A = "abba"       # input variant A for solution2 functions
INPUT_2B = "babbay"     # input variant B for solution2 functions


def runner():
    u"""Запускает выполнение всех задач"""
    print INPUT_1, ">>", hw2_solution1.squares_1(INPUT_1)
    print INPUT_1, ">>", hw2_solution1.squares_2(INPUT_1)
    print INPUT_1, ">>", hw2_solution1.squares_3(INPUT_1)

    print INPUT_2A, ">>", hw2_solution2.symmetry_1(INPUT_2A)
    print INPUT_2B, ">>", hw2_solution2.symmetry_2(INPUT_2B)


if __name__ == '__main__':
    runner()
    tests_for_hw2_solution1()
    tests_for_hw2_solution2()
    tests_for_hw2_solution3()
