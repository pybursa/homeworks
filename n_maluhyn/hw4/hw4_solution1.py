# -*- coding: utf8 -*-
from __future__ import division
u"""
Решение задачи#1: Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""

__author__ = "n_malukhin"
__email__ = "nikolay_malukhin@gmail.com"
__date__ = "2014-11-16"


def percentage_of_characters(input_text):
    input_text = input_text.lower()
    d = {}
    result = {}
    count = 0
    for (i, letter) in enumerate(input_text):
        count += 1
        if d.get(letter) == None:

            d[letter] = 1
        else:
            d[letter] += 1

    for letter in d:
        d[letter] = round(float(d[letter]) / count * 100, 1)
    return d

