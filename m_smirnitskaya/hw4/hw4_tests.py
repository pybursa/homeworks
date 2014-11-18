# -*- coding: utf8 -*-

u"""
Тесты на дз №4
"""

__author__ = "maria_s"
__email__ = "smirnitskayamp@gmail.com"
__date__ = "2014-11-15"

import hw4_solution1
import hw4_solution2

INPUT = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada."

def tests_for_solution1():
	u"""Tests for task 1"""
	assert hw4_solution1.solution1("A") == {'a': 100.0}
	assert hw4_solution1.solution1("ABCda") == {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
	assert hw4_solution1.solution1("AsBCda") == {'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7}
	assert hw4_solution1.solution1("q TyU#!{}.") == {'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0}
	assert sum(hw4_solution1.solution1("q TyU#!{}.").values()) == 100.0
	  
def tests_for_solution2():
	u"""Tests for task 2"""
	text = "Proin eget tortor risus."
	assert hw4_solution2.solution2(INPUT) == "Proin..."
	assert hw4_solution2.hw4_solution2(text) == "Proin eget tortor risus."
	assert hw4_solution2.solution2(text, 24) == "Proin eget tortor risus."
	assert hw4_solution2.solution2(text, 23) == "Proin eget tortor..."
	assert hw4_solution2.solution2(text, 13) == "Proin eget..."
	assert hw4_solution2.solution2(text, 6) == "Pro..."