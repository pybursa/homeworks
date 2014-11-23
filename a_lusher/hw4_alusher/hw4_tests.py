# -*- coding: utf-8 -*-
# Tests for Home Assignment 4

__author__ = "a_lusher"
__date__ = "2014-11-12"


import hw4_solution1
import hw4_solution2

def tests_for_hw4_solution1():
    u"""Тесты задачи 1"""
    assert hw4_solution1.text_analyzer("A") == {'a': 100.0}
    assert hw4_solution1.text_analyzer("ABCda") == {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
    assert hw4_solution1.text_analyzer("AsBCda") == {'a': 33.3,'b': 16.7, 'c': 16.7,'d': 16.7,'s': 16.7}
    assert hw4_solution1.text_analyzer("q TyU#!{}.") == {'q': 25.0,'t': 25.0,'y': 25.0,'u': 25.0}
    assert sum(hw4_solution1.text_analyzer("q TyU#!{}.").values()) == 100.0


def tests_for_hw4_solution2():
    u"""Тесты задачи 2"""
    text = "Proin eget tortor risus."
    assert hw4_solution2.cut_off(text) == "Proin eget tortor risus."
    assert hw4_solution2.cut_off(text, 24) == "Proin eget tortor risus."
    assert hw4_solution2.cut_off(text, 23) == "Proin eget tortor..."
    assert hw4_solution2.cut_off(text, 13) == "Proin eget..."
    assert hw4_solution2.cut_off(text, 6) == "Pro..."