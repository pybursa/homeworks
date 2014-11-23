#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #5.
Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = "Sergei Shybkoi"
__email__ = "heap_@mail.ru"
__date__ = "2014-11-18"

from hw5_task1 import Person
from hw5_tests import tests_for_hw5_solution1


def runner():
    u"""Запускает выполнение всех задач"""
    pupkin = Person("Pupkin", "Petr", "1982-11-20", "Petya Brick Top")
    pupkin.get_fullname()
    pupkin.get_age()
    print pupkin.nickname
    pushkin = Person("Pushkin", "Alexandr", "1799-05-26")
    print pushkin.birth_date, type(pushkin.birth_date)

if __name__ == '__main__':
    runner()
    tests_for_hw5_solution1()

