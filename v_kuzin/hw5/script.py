#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #5.
Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = "kuzin.valeriy"
__email__ = "kuzin.valeriy@gmail.com"
__date__ = "2014-11-19"


from hw5_solution1 import Person
from hw5_tests import tests_for_hw5_solution1


def runner():
    u"""Запускает выполнение всех задач"""
    input_data =("Sidorov", "Semen", "1980-12-31", "Senya")
    print input_data

    if len(input_data) == 3:
    	nicname = ''
    else:
    	nicname = input_data[3]

    result = Person(input_data[0], input_data[1], input_data[2], nicname)

    print result.birth_date

    print result.get_age()
    print result.get_fullname()


if __name__ == '__main__':
    runner()
    tests_for_hw5_solution1()