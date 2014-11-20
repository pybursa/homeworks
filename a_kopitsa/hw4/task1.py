#!/usr/bin/env python
# -*- coding: utf-8 -*-
# "ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}

import math

text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada."
text = sorted(text.lower())

x = "BACda"


def unique(list):
    """
    Упорядочиваю список: сортиру, удаляю дубликаты и привожу к нижнему регистру.
    """
    y = []
    for x in list.lower():
        if x not in y:
            y.append(x)
            y.sort()
    return y


def CountWord(var, text):
    """
    Формирую список количества повторяющихся чисел
    """
    count = 0
    listcount = []
    for i in var:
        for z in text:
            if z == i:
                count += 1
        listcount.append(count)
        count = 0

    return listcount


x = unique(x)
zz = {k: v for (k, v) in zip((x), CountWord(x, text))}
# Собрал словарь только с количеством встречающихся в тексте
print zz
