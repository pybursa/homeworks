# -*- coding: utf8 -*-

u"""
Тесты на ДЗ#5.
"""

__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-18"
__license__ = "GPL"
__version__ = "0.0.1"

import datetime

from hw5_solution1 import Person


def tests_for_hw5_solution1():
    u"""Тесты задачи 1"""
    petroff = Person("Petrov", "Petro", "1952-01-02")
    ivanoff = Person("Ivanov", "Ivan", "2000-10-20")
    sydoroff = Person("Sidorov", "Semen", "1980-12-31", "Senya")

    assert "first_name" in dir(petroff)
    assert "get_fullname" in dir(ivanoff)
    assert "nickname" not in dir(petroff)
    assert "nickname" in dir(sydoroff)

    assert petroff.surname == "Petrov"
    assert petroff.first_name == "Petro"
    assert petroff.get_fullname() == "Petrov Petro"
    assert sydoroff.nickname == "Senya"

    assert petroff.birth_date == datetime.date(1952, 01, 02)
    assert isinstance(petroff.birth_date, datetime.date)
    assert petroff.get_age() == "62"
