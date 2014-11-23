# # -*- coding: utf8 -*-

u"""
Задание 2: Послесловие...

УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов).
Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться
на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").

Текст:
Proin eget tortor risus.
Cras ultricies ligula sed magna dictum porta.
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

__author__ = 'Viktorov Eugene'
__email__ = 'jekafromua@gmail.com'
__date__ = '2014-11-16'

def limitation(inlet, run):
    u"""Фрагмент кода, который принимает строку и натуральное чило,
    величина которого определяет длинну сокращенной
    версии этой строки."""

    if run <= 3:
        out = '.' * run
        return out

    for i in reversed(range(run)):
        if len(inlet) <= run:
            out = inlet
            break
        if ' ' not in inlet[:i]:
            out = inlet[:i - 2] + '...'
            break
        if inlet[i - 2] == ' ':
            out = inlet[:i - 2] + '...'
            break
        continue
    return out
