# -*- coding: utf8 -*-

u"""
Решение задачи#1 ДЗ#4 - Частота буквы.

УСЛОВИЕ:
   Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}

Примечание: решение выполнено для кодировки ASCII  - поскольку в условии кодировка явно не задана.
"""


__author__ = "a_kushnaryoff"
__date__ = "2014-11-14"


import string


def letters_fq(text):
    text_dc = {}
    text_dc_result = {}

    for i in string.punctuation:
        text = text.replace(i, "").replace(" ", "").lower()

    for j in string.lowercase:
        k = text.count(j)
        if k > 0:
            text_dc.update({j: k})

    for k, v in text_dc.items():
        p = float(sum(text_dc.values()))/100
        text_dc_result.update({k: round(v/p, 1)})

    return text_dc_result
