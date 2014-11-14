#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание 8: A-a-a (бонусное)

УСЛОВИЕ:
Посчитать в тексте количество букв "a" при условии что она окружена согласными
("car") и она не является первой или последней буквой слова.

Текст:
Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh.

Согласные: все, кроме A, E, I, O, U, Y
"""

__author__ = 'wowkalucky'


TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta."""


import string


def countAs(text):
    vowels = "aeiouy"
    valid_letters = string.ascii_letters
    counter = 0
    for i, letter in enumerate(text[1:-1], start=1):
        if letter.lower() == vowels[0]:
            prev_letter = text[i-1].lower()
            next_letter = text[i+1].lower()
            if (prev_letter not in vowels and prev_letter in valid_letters
                and next_letter not in vowels and next_letter in valid_letters):
                counter += 1

    return counter


if __name__ == "__main__":
    test_text = """Abasa sdaadaalal."""
    print countAs(test_text)
    print countAs(TEXT)
