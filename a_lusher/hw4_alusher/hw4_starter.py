#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is the main script for Home Assignment 4.
# It loads modules one-by-one and run the tests as well
# 

__author__ = "a_lusher"
__date__ = "2014-11-12"


import hw4_solution1
import hw4_solution2
from hw4_tests import (tests_for_hw4_solution1)
from hw4_tests import (tests_for_hw4_solution2)

INPUT_1 = "Abbey"     # input for solution1 functions
INPUT_2 = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada."    # input for solution2 functions


def runner():
    # Starts execution of all solutions
    print INPUT_1, ">>", hw4_solution1.text_analyzer(INPUT_1)
    print INPUT_2, ">>", hw4_solution2.cut_off(INPUT_2,10)

if __name__ == '__main__':
    runner()
    tests_for_hw4_solution1()
    tests_for_hw4_solution2()
