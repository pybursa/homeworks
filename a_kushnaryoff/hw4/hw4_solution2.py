# -*- coding: utf8 -*-

u"""
Решение задачи#2 ДЗ#4 - Послесловие...

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


__author__ = "a_kushnaryoff"
__date__ = "2014-11-14"


import re


def string_cut(text, num=0):
    text_lst = text.split()
    ellipsis = "..."
    if len(text) <= num or num == 0:
        return text
    elif num <= 3:
        text = "Input limit number must be more than: 3"
        return text
    else:
        if len(text_lst[0]) + 1 >= num:
            text_prt = text_lst[0][:(num - 3)]
            text_out = text_prt + ellipsis
            return text_out
        else:
            text_prt = re.match('.*\s', text[:(num - 2)])
            text_out = text_prt.group(0).rstrip() + ellipsis
            return text_out
