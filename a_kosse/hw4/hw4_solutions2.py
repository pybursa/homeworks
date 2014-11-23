# -*- coding: utf-8 -*-
u"""
Решение задачи#2 ДЗ#4 - Послесловие...

УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо,
в случае, если текст не помещается в ограничение обрезать его, но при этом
слова не должны обрываться на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.
Donec rutrum congue leo eget malesuada.

Пример:
text = "Proin eget tortor risus."
limit = 24
output = "Proin eget tortor risus."
limit = 23
output = "Proin eget tortor..."
limit = 13
output = "Proin eget..."
limit = 6
output = "Pro..."
"""

__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-15"
__license__ = "GPL"
__version__ = "0.0.1"


def afterword(in_text, limit):
    """Main function homework #4.2"""
    if limit >= (len(in_text)):
        return in_text
    if '.' in in_text[:limit] and in_text[limit::-1].find('.') < 3:
        limit -= in_text[limit::-1].find('.')
        return in_text[:limit] + '.'

    limit -= 3
    if limit < 0:
        return "It's impossible!!! Limit < 3"
    if ' ' in in_text[:limit]:
        limit -= in_text[limit::-1].find(' ')
    return in_text[:limit] + '...'
