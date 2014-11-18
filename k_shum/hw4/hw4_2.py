#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо,
в случае, если текст не помещается в ограничение обрезать его, но при этом
слова не должны обрываться на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").

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

__author__ = "k.shym"
__email__ = "ks.shym@gmail.com"
__date__ = "2014-11-14"


def afterword(data, limit):
    u"""Получает строку data и ограничение длины limit"""
    dots = '...'
    lendots = len(dots)

    if limit <= lendots or len(data) <= limit:
        return data

    words = []
    temp = lendots

    for k, i in enumerate(data.split()):
        temp += len(i)
        if temp <= limit:
            words.append(i)
            temp += 1
            continue
        elif k is 0:
            words.append(i[0:limit-lendots])

        break

    return ' '.join(words) + '...'

if __name__ == '__main__':
    print afterword('Proin eget tortor risus.', 4)
    print afterword('Proin eget tortor risus.', 13)
