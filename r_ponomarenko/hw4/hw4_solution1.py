# -*- coding: utf8 -*-

u"""
Задание 1: Частота буквы.
УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные \
приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором \
эта буква встречается в тексте.
Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada.
Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""

__author__ = "rm_ponomarenko"
__email__ = "ponomarenko.roman@gmail.com"
__date__ = "2014-11-18"


import string


def percentage_1(s):
    """
    percentage_1(s) -> new dictionary where,
        key - letter in s,
        value - the percentage (rounded up to tens)
                in which this letter occurs in a text.

    Note: percentage_1(s) counts only ascii letters.

    For example:  "ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
    """
    chars_only = [item for item in list(s.lower())
                            if item in string.ascii_lowercase]
    unique_chars = list(set(chars_only))
    overall_chars_count = float(len(chars_only))
    return {ch : float("%.1f" %
                (chars_only.count(ch) / overall_chars_count * 100))
                        for ch in unique_chars }
