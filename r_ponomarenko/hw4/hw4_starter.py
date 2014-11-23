#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main script for HM#4.

This script is designed to run homework #4.
Also executes a set of tests from the test suite module.
"""

__author__ = "rm_ponomarenko"
__email__ = "ponomarenko.roman@gmail.com"
__date__ = "2014-11-18"


import hw4_solution1
import hw4_solution2
from hw4_tests import tests_for_hw4_solution1, tests_for_hw4_solution2


INPUT_1 = "AsBCda"
INPUT_2 = """Proin eget tortor risus. Cras ultricies ligula sed magna \
dictum porta. Donec rutrum congue leo eget malesuada."""


def runner():
    """Starts execution of all tasks"""
    print INPUT_1, ">>\n", hw4_solution1.percentage_1(INPUT_1)

    print INPUT_2, ">>\n", hw4_solution2.ellipsis_1(INPUT_2)
    print INPUT_2, ">>\n", hw4_solution2.ellipsis_1(INPUT_2, 10)
    print INPUT_2, ">>\n", hw4_solution2.ellipsis_1(INPUT_2, 15)


if __name__ == '__main__':
    runner()
    tests_for_hw4_solution1()
    tests_for_hw4_solution2()
