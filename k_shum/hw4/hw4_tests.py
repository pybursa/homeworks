#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""Тесты для ДЗ №4"""

__author__ = "k.shym"
__email__ = "ks.shym@gmail.com"
__date__ = "2014-11-14"

import hw4_1
import hw4_2


def tests_for_hw4_1():
    u"""Набор тестов для решения задачи 4.1"""
    assert hw4_1.letters('ABCda') == {
        'a': 40.0,
        'b': 20.0,
        'c': 20.0,
        'd': 20.0,
    }


def tests_for_hw4_2():
    u"""Набор тестов для решения задачи 4.2"""
    text = 'Proin eget tortor risus.'
    assert hw4_2.afterword(text, 24) == 'Proin eget tortor risus.'
    assert hw4_2.afterword(text, 23) == 'Proin eget tortor...'
    assert hw4_2.afterword(text, 13) == 'Proin eget...'
    assert hw4_2.afterword(text, 6) == 'Pro...'

if __name__ == '__main__':
    tests_for_hw4_1()
    tests_for_hw4_2()
