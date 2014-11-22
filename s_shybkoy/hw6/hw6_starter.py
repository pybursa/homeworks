#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #6.
"""

__author__ = "Sergei Shybkoi"
__copyright__ = "Copyright 2014, The Homework Project"
__email__ = "heap_@mail.ru"
__status__ = "Production"
__date__ = "2014-11-22"


from hw6_task1 import modifier


def runner():
    u"""Запускает выполнение всех задач"""
    print "Modifying file..."
    result_mes = modifier("data.csv")
    print result_mes

if __name__ == '__main__':
    runner()
