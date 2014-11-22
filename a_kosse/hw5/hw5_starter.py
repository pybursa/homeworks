#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#4.

Данный скрипт призван запускать на выполнение домашнее задание #5 путем
импортирования решений из соответствующих модулей. Также выполняется комплекс
тестов из модуля набора тестов.
"""

__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-15"
__license__ = "GPL"
__version__ = "0.0.1"


from hw5_tests import tests_for_hw5_solution1

if __name__ == '__main__':
    tests_for_hw5_solution1()
