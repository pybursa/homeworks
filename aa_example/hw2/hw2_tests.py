# -*- coding: utf8 -*-

u"""
Тесты на ДЗ#2.
"""

__author__ = "a_kosse"
__email__ = "kosse@mail.me"
__date__ = "2014-11-12"


import hw2_solution1
import hw2_solution2
# import hw2_solution3
# и так далее...


def tests_for_hw2_solution1():
    u"""Набор простых тестов для решения задачи 1 ДЗ#2"""
    assert hw2_solution1.squares_1([1, 2, 3]) == [1, 4, 9]  # "assert" проверяет является ли True переданное выражение
    assert hw2_solution1.squares_1((1, 2, 3)) == (1, 4, 9)
    assert hw2_solution1.squares_2([1, 2, 3]) == [1, 4, 9]
    assert hw2_solution1.squares_2((1, 2, 3)) == (1, 4, 9)
    assert hw2_solution1.squares_3([1, 2, 3]) == [1, 4, 9]
    assert hw2_solution1.squares_3((1, 2, 3)) == (1, 4, 9)


def tests_for_hw2_solution2():
    u"""Набор тестов для решения задачи 2 ДЗ#2"""
    assert hw2_solution2.symmetry_1("abba")
    assert hw2_solution2.symmetry_1("abrbrba")
    assert hw2_solution2.symmetry_1("abrbrrba") == False
    assert hw2_solution2.symmetry_2("abba")
    assert hw2_solution2.symmetry_2("abrbrba")
    assert hw2_solution2.symmetry_2("abrbrrba") == False


def tests_for_hw2_solution3():
    u"""Тесты на следующую задачу здесь..."""
    print "Tests for task 3 not implemented yet!"
    pass
