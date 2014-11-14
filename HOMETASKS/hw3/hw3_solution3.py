#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание 3: Реверс'em!

УСЛОВИЕ:
Изменить в тексте порядок следования:
- букв в словах;
- слов в предложениях;
- предложений в тексте.
Вывести модифицированный текст.

Текст:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta.
"""

__author__ = 'wowkalucky'


TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta."""


def simple_reverse_1(text):
    sentenses = text.split(".")
    sentenses.reverse()
    worded_sentenses = []
    for sentense in sentenses:
        words = sentense.split()
        words.reverse()
        worded_sentenses.append(words)
    result = []
    for sentense in worded_sentenses:
        for word in sentense:
            result.append(word[::-1])
    result = " ".join(result)
    return result


if __name__ == "__main__":
    test_text = """Abc dfg. Klm nopq. Rst xyz."""
    assert simple_reverse_1(test_text) == """zyx tsR qpon mlK gfd cbA"""
