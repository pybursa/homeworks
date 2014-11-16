#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Задание 1: Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.
Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""

__author__ = "Sergei Shybkoi"
__copyright__ = "Copyright 2014, The Homework Project"
__email__ = "heap_@mail.ru"
__status__ = "Production"
__date__ = "2014-11-15"

def let_frequency(txt):
    u"""Подсчитывает процент вхождения букв из текста в этот текст."""
    if type(txt) is str:
        txt = txt.lower()
        res_freq = {i: round(float(txt.count(i))/len(txt)*100, 1) for i in txt if i.isalpha()}
    else:
        res_freq = "Invalid input data!"
    return res_freq

if __name__ == '__main__':
    print let_frequency("ABCda")


