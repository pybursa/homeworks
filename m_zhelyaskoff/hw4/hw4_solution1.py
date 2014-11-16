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
        - считаем процент всех символов, что отвечают условию isalnum
        - отдельно считаем пробелы
        - отдельно считаем процент всех отальных символов, что не удовлетворили первым двум условиям
        - в общей длинне текста учитываются все символы

        Для решения задачи собираем словарь в котором для каждого символа
        расчитываем процент вхождения с помощью функци count
    """

    # переводим весь текст в нижний регистр
    text = text.lower()

    # Отдельно считаем пробелы
    # В общей длинне текста учитываются все символы
    length = len(text)
    spaces = {}
    number_of_spaces = text.count(" ")
    spaces["spaces"] = calc_percent(length, number_of_spaces, 1)
    print "spaces >>", spaces

    # Отдельно считаем процент вхождения символов пунктуации
    # В общей длинне текста учитываются все символы
    text_punctuation = filter(lambda ch: ch in string.punctuation, text)
    length = len(text)
    punctuations = {}
    for ch in set(text_punctuation):
        percent = calc_percent(length, text.count(ch), 1)
        punctuations[ch] = percent
    print "punctuations >>", punctuations

    # Удаление знаков пунктуации и пробелов
    alnum_text = filter(lambda ch: ch.isalnum(), text)

    # Длинну получаем из строки без символов пунктуации и пробелов,
    # потому как иначе результаты не пройдут проверку по файлу hw4_tests.py
    length = len(alnum_text)
    result = {}
    for ch in set(alnum_text):
        percent = calc_percent(length, alnum_text.count(ch), 1)
        result[ch] = percent

    return result





def percentage_2(text):
    u"""function(str) -> dict

        Считает процентное соотношение букв в тексте.
        Заглавные и строчные приравниваются.
        Возвращает словарь: ключ - буква, значение - процент (до десятых).
        - считаем процент всех символов, что отвечают условию isalnum
        - отдельно считаем пробелы
        - отдельно считаем процент всех отальных символов, что не \
          удовлетворили первым двум условиям
        - в общей длинне текста учитываются все символы

        Решение в два этапа: сначала собираем символы и их количество
        потом расчитываем процент их вхождения
    """

    # Инициализация переменных
    result = {}
    spaces = {}
    punctuations = {}
    text = text.lower()

    # расчет количества вхождений для всех видов символов
    for ch in text:
        if ch.isalnum():
            result[ch] = result.setdefault(ch, 0) + 1
        elif ch == ' ':
            spaces["spaces"] = spaces.setdefault("spaces", 0) + 1
        else:
            punctuations[ch] = punctuations.setdefault(ch, 0) + 1

    # расчент процентного показателя для всех групп символов
    # процент вхождения пробелов
    for key in spaces.keys():
        spaces[key] = calc_percent(len(text), spaces[key], 1)
    print "spaces >>", spaces

    # прцоент вхождения символов пунктукции
    for key in punctuations.keys():
        punctuations[key] = calc_percent(len(text), punctuations[key], 1)
    print "punctuations >>", punctuations

    # Вычисляем процент вхождения цифр и букв
    # Длинну получаем из строки без символов пунктуации и пробелов,
    # потому как иначе результаты не пройдут проверку по файлу hw4_tests.py
    alnum_text = filter(lambda ch: ch.isalnum(), text)
    length = len(alnum_text)
    for key in result.keys():
        result[key] = calc_percent(length, result[key], 1)

    return result



if __name__ == '__main__':
    test_text = "q TyU#!{}."
    percentage_1(test_text) == {'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0}
    percentage_2(test_text) == {'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0}
    print "Ok"
