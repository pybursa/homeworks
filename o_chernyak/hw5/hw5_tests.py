# -*- coding: utf8 -*-

u"""
Тесты на ДЗ#5.
Непонятно почему тесты не работают
"""

__author__ = "o_chernyak"
__email__ = "olgache73@gmail.com"
__date__ = "2014-11-20"

from datetime import date, datetime
from hw5_task1 import Person

def tests_for_hw5():
    u"""Тесты задачи 1"""
    petrov = Person("Petrov", "Peter", "1979-11-30")
    sydorov = Person("Sidorov", "Sid", "1977-01-17", "Sider")

    assert "first_name" in dir(petrov)
    assert "get_fullname" in dir(petrov)
    assert "nickname" not in dir(petrov)
    assert "nickname" in dir(sydorov)

    assert petrov.surname == "Petrov"
    assert petrov.first_name == "Peter"
    assert petrov.get_fullname() == "Petrov Peter"
    assert sydorov.nickname == "Sider"

    assert petrov.get_age() == "34"
