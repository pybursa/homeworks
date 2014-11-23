#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.

Данный скрипт призван запускать на выполнение домашнее задание #5.
Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = "a_kushnaryoff"
__date__ = "2014-11-19"


from hw5_solution1 import Person
from hw5_tests import tests_for_hw5_solution1


def runner():
    u"""Запускает выполнение всех задач"""
    sydoroff = Person("Sidorov", "Semen", "1980-12-31", "Senya")
    print sydoroff.get_fullname()
    print sydoroff.nickname
    print sydoroff.get_age()

    petroff = Person("Petrov", "Petro", "1952-01-02")
    print petroff.get_fullname()
    print petroff.get_age()


if __name__ == '__main__':
    runner()
    tests_for_hw5_solution1()
