# -*- coding: utf-8 -*-

u"""
Решение задачи#1 ДЗ#4 - Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""

__author__ = 'm_shalamov'


from re import sub


def check_letters_percent_frequency_in_text(source_string):
    u"""Основной скрипт расчитатывающий процентное соотношение букв в тексте"""
    prepared_string = sub('[\x20\x2e\W]*', '', source_string.lower())

    char_count = len(prepared_string)

    result_dict = dict()

    for char_item in prepared_string:
        if char_item not in result_dict:
            result_dict[char_item] = 1
        else:
            result_dict[char_item] += 1

    for dict_item, dict_item_value in result_dict.iteritems():
        result_dict[dict_item] = round((float(dict_item_value)/char_count)*100, 1)

    return result_dict
