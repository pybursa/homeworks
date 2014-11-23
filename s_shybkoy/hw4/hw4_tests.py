#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Тесты на ДЗ#4.
"""

__author__ = "Sergei Shybkoi"
__copyright__ = "Copyright 2014, The Homework Project"
__email__ = "heap_@mail.ru"
__status__ = "Production"
__date__ = "2014-11-15"

import hw4_task1
import hw4_task2

def tests_for_hw4_task1():
    u"""Набор тестов для решения задачи 1 ДЗ#4"""
    assert hw4_task1.let_frequency("ABCda") == {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
    assert hw4_task1.let_frequency(234) == "Invalid input data!"

def tests_for_hw4_task2():
    u"""Набор тестов для решения задачи 2 ДЗ#4"""
    assert hw4_task2.limit_text("Proin eget tortor risus.", 13) == "Proin eget..."
    assert hw4_task2.limit_text("Proin eget tortor risus.", 23) == "Proin eget tortor..."
    assert hw4_task2.limit_text(234, -1) == "Invalid input data!"


