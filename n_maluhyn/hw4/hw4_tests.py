# -*- coding: utf8 -*-

u"""
Тесты на ДЗ#4.
"""

__author__ = "n_malukhin"
__email__ = "nikolay_malukhin@gmail.com"
__date__ = "2014-11-16"


import hw4_solution1
import hw4_solution2
# import hw4_solution1


def tests_for_hw4_solution1():
    assert hw4_solution1.percentage_of_characters("ABCda") == {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}

def tests_for_hw4_solution2():
    assert hw4_solution2.afterword("Proin eget tortor risus.", 24) == 'Proin eget tortor risus.'
    assert hw4_solution2.afterword("Proin eget tortor risus.", 23) == 'Proin eget tortor...'
    assert hw4_solution2.afterword("Proin eget tortor risus.", 13) == 'Proin eget...'
    assert hw4_solution2.afterword("Proin eget tortor risus.", 6) == 'Proin...'
    pass



