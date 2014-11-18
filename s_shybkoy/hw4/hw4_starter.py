#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#4.

Данный скрипт призван запускать на выполнение домашнее задание #4 путем импортирования решений из соответствующих
модулей. Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = "Sergei Shybkoi"
__copyright__ = "Copyright 2014, The Homework Project"
__credits__ = ["Sergei Shybkoi"]
__license__ = "ShS"
__version__ = "0.0.1"
__maintainer__ = "Sergei Shybkoi"
__email__ = "heap_@mail.ru"
__status__ = "Production"
__date__ = "2014-11-15"

import hw4_task1
import hw4_task2
from hw4_tests import (tests_for_hw4_task1, tests_for_hw4_task2)

INPUT_TEXT = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. " \
             "Donec rutrum congue leo eget malesuada."
INPUT_LIMIT = 13

def runner():
    u"""Запускает выполнение всех задач"""
    print INPUT_TEXT, ">>", hw4_task1.let_frequency(INPUT_TEXT)
    print INPUT_TEXT, "LIMIT:", str(INPUT_LIMIT), ">>", hw4_task2.limit_text(INPUT_TEXT, INPUT_LIMIT)

if __name__ == '__main__':
    runner()
    tests_for_hw4_task1()
    tests_for_hw4_task2()
