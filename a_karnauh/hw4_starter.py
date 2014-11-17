#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#4.
Данный скрипт призван запускать на выполнение домашнее задание #4.
Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = "anna-karnaukh"
__email__ = "anna.karnaukh1@gmail.com"
__date__ = "2014-11-16"

import hw4_solution1
import hw4_solution2
from hw4_tests import tests_for_hw4_solution1, tests_for_hw4_solution2

INPUT_1 = "AsBCda"
INPUT_2 = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada."""

def runner():
	u"""Запускает выполнение всех задач"""
	print INPUT_1, ">>\n", hw4_solution1.frequency_of_letters(INPUT_1)
	print INPUT_2, ">>\n", hw4_solution2.afterword(INPUT_2)
	print INPUT_2, ">>\n", hw4_solution2.afterword(INPUT_2, 10)
	print INPUT_2, ">>\n", hw4_solution2.afterword(INPUT_2, 15)

if __name__ == '__main__':
	runner()
	tests_for_hw4_solution1()
	tests_for_hw4_solution2()