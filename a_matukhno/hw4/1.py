#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Задание 1: Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква
встречается в тексте.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue
leo eget malesuada.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}

================================================================================
"""

__author__ = 'Andrey Matukhno'

text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue \
leo eget malesuada."

test1 = "A"
test2 = "ABCda"
test3 = "AsBCda"
test4 = "q TyU#!{}."


def letter_frequency(text):

    freq_dict = {}
    outer_string = ""

    for char in text:
        if char.isalpha():
            outer_string += char
    text = outer_string

    for char in text:
        if char.lower() not in freq_dict:
            freq_dict[char.lower()] = 1.0
        elif char.lower() in freq_dict:
            freq_dict[char.lower()] += 1.0

    for char in freq_dict:
        freq_dict[char] = round(freq_dict[char] / text.__len__() * 100, 1)

    return freq_dict


if __name__ == '__main__':
    assert letter_frequency(test1) == {'a': 100.0}
    assert letter_frequency(test2) == {'a': 40.0, 'c': 20.0, 'b': 20.0, 'd': 20.0}
    assert letter_frequency(test3) == {'a': 33.3, 's': 16.7, 'b': 16.7, 'c': 16.7, 'd': 16.7}
    assert letter_frequency(test4) == {'q': 25.0, 'y': 25.0, 'u': 25.0, 't': 25.0}
    assert sum(letter_frequency(test4).values()) == 100.0
    print letter_frequency(text)
    print sum(letter_frequency(text).values())