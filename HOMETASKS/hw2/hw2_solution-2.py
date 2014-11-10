# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 2: Симметрия.

УСЛОВИЕ:
Фрагмент кода, который принимает строку и определяет симметрична ли строка.
(Возвращает True или False).

Пример:
"abba" >> True
"arbat" >> False
"""


def symmetry_1(string):
    return string == string[::-1]


def symmetry_2(string):
    while len(string) > 1:
        if string[0] != string[-1]:
            return False
        string = string[1:-1]
    return True


if __name__ == "__main__":
    assert symmetry_1("abba")
    assert symmetry_1("abrbrba")
    assert symmetry_1("abrbrrba") == False
    assert symmetry_2("abba")
    assert symmetry_2("abrbrba")
    assert symmetry_2("abrbrrba") == False
