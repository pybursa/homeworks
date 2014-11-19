# coding=utf-8

u"""
УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""


from string import lowercase


def percentage_1(text):
    letter_lenght = 0
    result = {}
    for letter in text.lower():
        if letter in lowercase:
            letter_lenght += 1
            result[letter] = result.get(letter, 0) + 1
    for letter in result.keys():
        result[letter] = round(float(result[letter]) / letter_lenght * 100, 1)
    return result
