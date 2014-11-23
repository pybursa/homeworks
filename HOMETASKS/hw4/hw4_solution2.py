# -*- coding: utf8 -*-

u"""
Задание 2: Послесловие...

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

__author__ = "wowkalucky"
__email__ = "wowkalucky@gmail.com"
__date__ = "2014-11-14"


def ellipsis_1(text, limit=0):
    u"""Решение через индексы концов слов..."""
    assert limit not in [1, 2], "Invalid limit argument!"
    ellipsis = "..."
    if not limit or limit >= len(text):
        return text
    trimmed_text = ""
    for i, word in enumerate(text.split()):
        trimmed_text += word + " "
        if len(trimmed_text[:-1] + ellipsis) > limit:
            if i == 0:
                return word[: limit-len(ellipsis)] + ellipsis
            return trimmed_text[:-len(word)-2] + ellipsis
