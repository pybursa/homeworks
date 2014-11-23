# -*- coding: utf8 -*-

u"""
Решение задачи#2 ДЗ#4 -Послесловие...

УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.

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

__author__ = "n_malukhin"
__email__ = "nikolay_malukhin@gmail.com"
__date__ = "2014-11-16"


def afterword(text, limit):
    if len(text) <= limit:
        return text
    if text[limit] == ' ':
        text = text[0:limit] + '...'
    else:
        end_of_line = 0
        text = text[0: limit]
        for i, e in reversed(list(enumerate(text))):
            if e == ' ':
                end_of_line = i
                break
        text = text[0: end_of_line] + '...'

    return text
