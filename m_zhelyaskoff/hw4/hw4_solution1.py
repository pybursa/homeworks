#!/usr/bin/env python
# -*- coding: utf-8 -*-


u"""
Задание 1: Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные \
приравниваются. Вывести словарь: ключ - буква, значение - процент \
(до десятых), в котором эта буква встречается в тексте.


Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada.
"""

__author__ = "Mihail Zhelyaskov aka m_zhelyaskoff"
__copyright__ = "Copyright 2014, The Homework Project"
__version__ = "0.0.1"
__maintainer__ = "Mihail Zhelyaskov"
__email__ = "mzhelyaskov@yandex.ru"
__status__ = "Production"



TEXT = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum \
porta. Donec rutrum congue leo eget malesuada."""


import string

from hw4_utils import calc_percent




def percentage_1(text):
    u"""function(str) -> dict

        Считает процентное соотношение букв в тексте.
        Заглавные и строчные приравниваются.
        Возвращает словарь: ключ - буква, значение - процент (до десятых).

        Для решения задачи собираем словарь в котором для каждого символа
        расчитываем процент вхождения с помощью функци count
    """

    # delete punctuation and spaces
    text = filter(lambda ch: ch.isalpha(), text)
    text = text.lower()

    # create a dictionary
    length = len(text)
    result = {}
    for ch in set(text):
        percent = calc_percent(length, text.count(ch), 1)
        result[ch] = percent
    return result




def percentage_2(text):
    u"""function(str) -> dict

        Считает процентное соотношение букв в тексте.
        Заглавные и строчные приравниваются.
        Возвращает словарь: ключ - буква, значение - процент (до десятых).

        Решение в два этапа: сначала собираем символы и их количество
        потом расчитываем процент их вхождения
    """

    # delete punctuation and spaces
    text = filter(lambda ch: ch.isalpha(), text)
    text = text.lower()

    # create a dictionary
    length = len(text)
    result = {}

    # count the number of occurrences
    for ch in text:
        result[ch] = result.setdefault(ch, 0) + 1

    # calculate the percentage
    for key in result.keys():
        result[key] = calc_percent(length, result[key], 1)

    return result



if __name__ == '__main__':
    test_text = "q TyU#!{}."
    percentage_1(test_text) == {'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0}
    percentage_2(test_text) == {'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0}
    print "Ok"
