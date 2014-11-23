# -*- coding: utf8 -*-

u"""
Тесты на ДЗ#4.
"""

__author__ = 'm_shalamov'


import task_one


def tests_for_hw4_task_one():
    u"""Набор простых тестов для решения задачи 1 ДЗ#4"""
    assert task_one.check_letters_percent_frequency_in_text("A") == {'a': 100.0}
    assert task_one.check_letters_percent_frequency_in_text("ABCda") == {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
    assert task_one.check_letters_percent_frequency_in_text("AsBCda") == {'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7,
                                                                          's': 16.7}
    assert task_one.check_letters_percent_frequency_in_text("q TyU#!{}.") == {'q': 25.0, 't': 25.0, 'y': 25.0,
                                                                              'u': 25.0}
    assert sum(task_one.check_letters_percent_frequency_in_text("q TyU#!{}.").values()) == 100.0
