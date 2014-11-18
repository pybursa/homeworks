# # -*- coding: utf8 -*-

u"""
решение задачи №1 ДЗ №1 -  Частота буквы.


УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте.
Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых),
в котором эта буква встречается в тексте.

Текст:
Proin eget tortor risus.
Cras ultricies ligula sed magna dictum porta.
Donec rutrum congue leo eget malesuada.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""

__author__ = 'Viktorov Eugene'
__email__ = 'jekafromua@gmail.com'
__date__ = '2014-11-16'


def percent(inlet):

    len_of_text = len(inlet)
    out = {}
    inlet = inlet.lower()

    for i in inlet:
        if i.isalnum():
            out[i] = out.pop(i, 0) + 1
        else:
            out['other'] = 1 + out.pop('other', 0)

    for i in out.keys():
        out[i] = float(out[i]) / len_of_text * 100
        out[i] = float(format(out[i], '.1f'))

    return out
