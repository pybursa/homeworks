# -*- coding: utf8 -*-

u"""
Тесты на ДЗ#2.
"""

__author__ = "anna-karnaukh"
__email__ = "anna.karnaukh1@gmail.com"
__date__ = "2014-11-16"

import hw4_solution1
import hw4_solution2

def tests_for_hw4_solution1():
	u"""Тесты задачи 1"""
	assert hw4_solution1.frequency_of_letters("A") == {'a': 100.0}
	assert hw4_solution1.frequency_of_letters("ABCda") == {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
	assert hw4_solution1.frequency_of_letters("AsBCda") == {'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7}
	assert hw4_solution1.frequency_of_letters("q TyU#!{}.") == {'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0}
	assert sum(hw4_solution1.frequency_of_letters("q TyU#!{}.").values()) == 100.0

def tests_for_hw4_solution2():
	u"""Тесты задачи 2"""
	text = "Proin eget tortor risus."
	assert hw4_solution2.afterword(text) == "Proin eget tortor risus."
	assert hw4_solution2.afterword(text, 24) == "Proin eget tortor risus."
	assert hw4_solution2.afterword(text, 23) == "Proin eget tortor..."
	assert hw4_solution2.afterword(text, 13) == "Proin eget..."
	assert hw4_solution2.afterword(text, 6) == "Pro..."
