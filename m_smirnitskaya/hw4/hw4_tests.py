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
	assert hw4_solution1.solution1(INPUT) == {'a': 7.3, ' ': 14.5, 'c': 4.5,\
	 'e': 9.1, 'd': 3.6, 'g': 4.5, 'i': 5.5, 'm': 3.6, 'l': 4.5, 'o': 6.4,\
	  'n': 3.6, 'p': 1.8, 's': 5.5, 'r': 8.2, 'u': 7.3, 't': 7.3, '.': 2.7}
	  
def tests_for_solution2():
	assert hw4_solution2.solution2(INPUT) == "Proin..."