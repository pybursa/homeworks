#!/usr/bin/env python2
# coding=utf-8
"""
Simple test suite for PyBursa HW4"
"""
from hw4_solution1 import task01
from hw4_solution2 import task02


def tests_for_hw4_solution1():
    """Simple tests for task01 PyBursa HW4"""
    assert task01("ABCda") == {'a': 40.0, 'c': 20.0, 'b': 20.0, 'd': 20.0}


def tests_for_hw4_solution2():
    """Simple tests for task02 PyBursa HW4"""
    text = "Proin eget tortor risus."
    assert task02(text, 24) == text
    assert task02(text, 23) == "Proin eget tortor..."
    assert task02(text, 13) == "Proin eget..."
    assert task02(text, 6) == "Pro..."


if __name__ == '__main__':
    tests_for_hw4_solution1()
    tests_for_hw4_solution2()

