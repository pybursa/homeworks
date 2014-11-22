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

__author__ = "rm_ponomarenko"
__email__ = "ponomarenko.roman@gmail.com"
__date__ = "2014-11-18"


import string


def ellipsis_1(text, limit=-1):
    """
    ellipsis_1(text, limit) -> trimmed text,
        text - text to trim,
        limit - text limit after trimming.
    """
    if limit == -1 or limit >= len(text):
        return text
    appender = '...'
    first_word_len = [len(item) for item in text.split()][0]
    if first_word_len + len(appender) > limit:
        return ''.join(text.split()[0][:limit - len(appender)]) + appender
    limited_text = text[:limit]
    trimmed_text = limited_text[:len(limited_text) - len(appender)]
    if text[limit - len(appender)] in string.whitespace \
                    or text[limit - len(appender)] in string.punctuation:
        return trimmed_text + appender
    end = [index for index in range(len(trimmed_text))
                    if trimmed_text[index] in string.whitespace][-1]
    return trimmed_text[:end] + appender
