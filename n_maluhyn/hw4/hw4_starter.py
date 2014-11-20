#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#4.

"""

__author__ = "n_malukhin"
__email__ = "nikolay_malukhin@gmail.com"
__date__ = "2014-11-16"


import hw4_solution1
import hw4_solution2
from hw4_tests import (tests_for_hw4_solution1, tests_for_hw4_solution2)


INPUT_1 = "ABCd +-llklkla"
INPUT_text = "Proin eget tortor risus."
INPUT_limit_1 = 23
INPUT_limit_2 = 7
INPUT_limit_3 = 5
INPUT_limit_4 = 4


def runner():
    u"""Запускает выполнение всех задач"""
    print INPUT_1, ">>", hw4_solution1.percentage_of_characters(INPUT_1)

    print INPUT_text + ' limit:' + str(INPUT_limit_1), ">>", hw4_solution2.afterword(INPUT_text, INPUT_limit_1)
    print INPUT_text + ' limit:' + str(INPUT_limit_2), ">>", hw4_solution2.afterword(INPUT_text, INPUT_limit_2)
    print INPUT_text + ' limit:' + str(INPUT_limit_3), ">>", hw4_solution2.afterword(INPUT_text, INPUT_limit_3)
    print INPUT_text + ' limit:' + str(INPUT_limit_4), ">>", hw4_solution2.afterword(INPUT_text, INPUT_limit_4)



if __name__ == '__main__':
    runner()
    tests_for_hw4_solution1()
    tests_for_hw4_solution2()
