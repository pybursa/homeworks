#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""Основной скрипт запуска ДЗ №4"""

__author__ = "k.shym"
__email__ = "ks.shym@gmail.com"
__date__ = "2014-11-14"

import hw4_1
import hw4_2
from hw4_tests import tests_for_hw4_1, tests_for_hw4_2


def runner():
    u"""Запускает выполнение всех задач"""
    data = 'ABCda'
    print data, '>>', hw4_1.letters(data), '\n'

    text = 'Proin eget tortor risus.'
    data = [text, 24]
    print data, '>>', hw4_2.afterword(*data)
    data = [text, 23]
    print data, '>>', hw4_2.afterword(*data)
    data = [text, 13]
    print data, '>>', hw4_2.afterword(*data)
    data = [text, 6]
    print data, '>>', hw4_2.afterword(*data)

if __name__ == '__main__':
    runner()
    tests_for_hw4_1()
    tests_for_hw4_2()
