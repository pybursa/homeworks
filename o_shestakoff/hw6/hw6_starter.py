#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #6.
"""

__author__ = "wowkalucky"
__email__ = "wowkalucky@gmail.com"
__date__ = "2014-11-17"


from hw6_solution1 import modifier


def runner():
    u"""Запускает выполнение всех задач"""
    print "Modifying file..."
    modifier("data.csv")
    print "Modified successfully!"

if __name__ == '__main__':
    runner()