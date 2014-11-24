#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.
Данный скрипт призван запускать на выполнение домашнее задание #6.
"""

__author__ = "Viktorov Eugene"
__email__ = "jekafromua@gmail.com"
__date__ = "2014-11-23"


import hw6_solution1


def runner():
    u"""Запускает выполнение всех задач"""
    
    hw6_solution1.modifer('data.csv')


if __name__ == '__main__':
    runner()
