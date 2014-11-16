# coding=utf-8
u"""
Task 01 PyBursa HW4

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""
from string import lowercase


def task01(text):
    """
    Computes frequency of every letter in input text
    :param text: text to find letter frequency
    :return:dictionary letter:frequency
    """
    text_length = 0
    result_data = {}
    for letter in text.lower():
        if letter in lowercase:
            text_length += 1
            result_data[letter] = result_data.get(letter, 0) + 1
    for letter in result_data.keys():
        result_data[letter] = round(float(result_data[letter]) / text_length * 100, 1)
    return result_data

