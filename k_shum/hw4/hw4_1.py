#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Задание 1: Частота буквы.
УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные
приравниваются. Вывести словарь: ключ - буква, значение - процент (до десятых),
в котором эта буква встречается в тексте.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""

__author__ = "k.shym"
__email__ = "ks.shym@gmail.com"
__date__ = "2014-11-14"

import re


def letters(data):
    u"""Получает строку data и считает процентное соотношение букв в тексте"""
    result = {}

    data = re.sub('[^a-z]', '', data.lower())

    for i in data:
        if i not in result:
            result[i] = 0

        result[i] += 1

    l = float(len(data))

    for i in result.keys():
        result[i] = round(100 / l * float(result[i]), 1)

    return result

if __name__ == '__main__':
    print letters('ABCda')
