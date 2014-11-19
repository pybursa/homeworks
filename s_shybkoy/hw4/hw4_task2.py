#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Задание 2: Послесловие...

УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине (исключение первое слово),
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

__author__ = "Sergei Shybkoi"
__copyright__ = "Copyright 2014, The Homework Project"
__email__ = "heap_@mail.ru"
__status__ = "Production"
__date__ = "2014-11-15"

TEXT = "Proin eget tortor risus."

def limit_text(txt, limit):
    u"""Красиво обрезаем текст."""
    if type(txt) is str and type(limit) is int and limit > 0:
        if limit <= 3:
            return "..."
        if limit >= len(txt):
            return txt
        if limit-1 <= txt.find(' '):
            return txt[:limit-3] + "..."
        t_limit = txt[:limit][-1::-1]
        sp_num = t_limit.find(' ')
        t_limit = t_limit[sp_num:]
        for i, v in enumerate(t_limit):
            if v.isalpha():
                break
        t_limit = t_limit[i:][-1::-1] + "..."
        return t_limit
    else:
        return "Invalid input data!"

if __name__ == '__main__':
    print limit_text(TEXT, 6)
