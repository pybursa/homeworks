# -*- coding: utf8 -*-

u"""
Тесты на ДЗ#4.
"""

__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-15"
__license__ = "GPL"
__version__ = "0.0.1"



import hw4_solutions1
import hw4_solutions2

def tests_for_hw4_solution1():
    u"""Набор простых тестов для решения задачи 1 ДЗ#4"""
    assert hw4_solutions1.freq_letter("ABCda") == {'a': 40.0,
     'b': 20.0, 'c': 20.0, 'd': 20.0}


def tests_for_hw4_solution2(IN_TEXT):
    u"""Набор тестов для решения задачи 2 ДЗ#4"""
    assert hw4_solutions2.afterword(IN_TEXT, 24) == "Proin eget tortor risus."
    assert hw4_solutions2.afterword(IN_TEXT, 23) == "Proin eget tortor..."
    assert hw4_solutions2.afterword(IN_TEXT, 13) == "Proin eget..."
    assert hw4_solutions2.afterword(IN_TEXT, 6) == "Pro..."


