#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска дз №4

Скрипт запускает на выполнение домашнее задание №4 путем импортирования решений из соотв. модулей.
Дополнительно выполняется комплекс тестов из модуля набора тестов.

"""

__author__ = "maria_s"
__email__ = "smirnitskayamp@gmail.com"
__date__ = "2014-11-15"

import hw4_solution1
import hw4_solution2
from hw4_tests import (tests_for_solution1, tests_for_solution2)

INPUT = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada."

def starter():
	print "------- TASK #1 -------"
	print INPUT
	print " >> "
	print hw4_solution1.solution1("INPUT")
	print "------- TASK #2 -------"
	print INPUT
	print " >> "
	print hw4_solution2.solution2(INPUT, 34)


if __name__ == "__main__":
	starter()
	tests_for_solution1()
