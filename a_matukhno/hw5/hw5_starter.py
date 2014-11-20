#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.

Данный скрипт призван запускать на выполнение домашнее задание #5.
Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = "wowkalucky"
__email__ = "wowkalucky@gmail.com"
__date__ = "2014-11-17"


import hw5_solution1
from hw5_tests import tests_for_hw5_solution1


def runner():
    u"""Запускает выполнение всех задач"""
    # здесь можно запустить что-то
    me = hw5_solution1.Person('Matukhno', 'Andrey', '1985-02-04')
    print me.birth_date
    print me.get_age()
    print me.get_fullname()
    print dir(me)

if __name__ == '__main__':
    runner()
    tests_for_hw5_solution1()
