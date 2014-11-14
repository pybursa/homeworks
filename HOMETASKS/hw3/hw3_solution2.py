#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание 2: Самое длинное слово.

УСЛОВИЕ:
Найти слово максимальной длины в тексте.
Вывести это слово. Если таких слов несколько - вывести все.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
"""

__author__ = 'wowkalucky'


TEXT = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. \
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."""


def longest_word_1(text):
    words = text.split()
    clean_words = [word.rstrip('.,:') for word in words]
    max_len = max(len(word) for word in clean_words)
    return [word for word in clean_words if len(word) == max_len]


if __name__ == "__main__":
    assert len(longest_word_1(TEXT)) == 4
