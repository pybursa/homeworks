# -*- coding: utf-8 -*-

u"""
Модуль утилит для домашнего задания №4
"""

__author__ = "Mihail Zhelyaskov aka m_zhelyaskoff"
__copyright__ = "Copyright 2014, The Homework Project"
__version__ = "0.0.1"
__maintainer__ = "Mihail Zhelyaskov"
__email__ = "mzhelyaskov@yandex.ru"
__status__ = "Production"


import math


def calc_percent(rate, x=1, ndigits=0):
    u"""Вычисляет процентное значение x от rate

    Описание аргументов:
    rate -- значение которое соответствует 100 процентам
    x -- значение для которого вычисляется процент (default 1)
    ndigits -- округлить результат с заданной точностью в десятичных цифрах (default 0)
    """
    res = round(100.0 * x / rate, ndigits)
    return res
