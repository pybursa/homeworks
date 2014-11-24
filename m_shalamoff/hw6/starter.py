#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #6.
"""

__author__ = "m_shalamov"


from task_one import modifier

FILE_NAME = "data.csv"


def runner():
    u"""Запускает выполнение всех задач"""
    print "Modifying file..."
    modifier(FILE_NAME)
    print "Modified successfully!"

if __name__ == '__main__':
    runner()
