# -*- coding: utf8 -*-
u"""
Тесты на ДЗ#4.
"""

__author__ = "OlgaChernyak"
__email__ = "olgache73@gmail.com"
__date__ = "2014-11-16"

import hw4_task1

def tests_for_hw4_task1():
    u"""Тесты задачи 1"""
    assert hw4_task1.hw4_percentage(text_in) == {'a': 7.0, ' ': 15.0, 'c': 5.0, 'e': 9.0, 'd': 4.0, 'g': 5.0, 'i': 5.0, 'm': 4.0, 'l': 5.0, 'o': 6.0, 'n': 4.0, 'p': 2.0, 's': 5.0, 'r': 8.0, 'u': 7.0, 't': 7.0, '.': 3.0}
    assert sum(hw4_task1.hw4_percentage(text_in).values()) == 100.0

