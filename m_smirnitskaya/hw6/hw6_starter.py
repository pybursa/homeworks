#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #6.
"""

__author__ = "marie_s"
__email__ = "smirnitskayamp@gmail.com"
__date__ = "2014-11-21"


from hw6_solution1 import modifier


def runner():
    u"""Запускает выполнение всех задач"""
    print "Modifying file..."
    modifier("data.csv")
    print "Modified successfully!"

if __name__ == '__main__':
    runner()