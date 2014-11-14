#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание 1: И снова гласные.

УСЛОВИЕ:
Посчитать количество гласных в каждом слове текста.
Вывести максимальное количество гласных в одном слове.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.

Гласные: A, E, I, O, U, Y
"""

__author__ = 'wowkalucky'


TEXT = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. \
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."""

VOWELS = "AEIOUY"

def max_vowels_1(text, vowels):
    words = text.split()
    text_vowels_count = []
    for word in words:
        word_vowels_count = 0
        for letter in word:
            if letter.upper() in vowels:
                word_vowels_count += 1
        text_vowels_count.append(word_vowels_count)
    return max(text_vowels_count)


if __name__ == "__main__":
    assert max_vowels_1(TEXT, VOWELS) == 5
