# coding=utf8

u"""
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


__author__ = "a_cherkashin"


import re


def ellipsis_1(text, num=0, ellipsis = "..."):
    text_list = text.split()
    if len(text) <= num or num == 0:
        return text
    elif num <= len(ellipsis):
        return "Your input is so strange. Please, enter number greater than " + str(len(ellipsis))
    else:
        if len(text_list[0]) + 1 >= num:
            text_prt = text_list[0][:(num - 3)]
            text_out = text_prt + ellipsis
            return text_out
        else:
            text_prt = re.match('.*\s', text[:(num - 2)])
            text_out = text_prt.group(0).rstrip() + ellipsis
            return text_out

