#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ#4.
Данный скрипт призван запускать на выполнение домашнее задание #4 путем импортирования решений из соответствующих
модулей. Также выполняется комплекс тестов из модуля набора тестов.
"""

__author__ = 'm_shalamov'


import task_one
from tests import tests_for_hw4_task_one
# from .operation_with_files import get_string_line


FILE_PATH = '../source/source_data_3.txt'
# SOURCE_STRING = get_string_line(FILE_PATH)


def runner():
    u"""Запускает выполнение всех задач"""
    print task_one.check_letters_percent_frequency_in_text("aaaadd")


if __name__ == '__main__':
    runner()
    tests_for_hw4_task_one()
