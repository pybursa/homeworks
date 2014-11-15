# -*- coding: utf-8 -*-
u"""
Решение задачи#1 ДЗ#4 - Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные
приравниваются. Вывести словарь: ключ - буква, значение - процент (до
десятых), в котором эта буква встречается в тексте.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.
Donec rutrum congue leo eget malesuada.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""

__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-15"
__license__ = "GPL"
__version__ = "0.0.1"


def freq_letter(in_text):
    """Main function homework #4.1"""
    result = {}
    letters = 0
    in_text = in_text.lower()
    for i in in_text:
        if i.isalpha():
            letters += 1
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
    for i in result:
        result[i] = result[i] * 100.0 / letters
    return result
