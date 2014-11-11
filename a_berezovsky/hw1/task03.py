# -*- coding: utf-8 -*-
"""
Задание 3: подстчет вхождений подстроки.

УСЛОВИЕ:
Реализовать подсчеы количества вхождений подстроки "wow" в строке.

ВХОД: строка
ВЫХОД: число вхождений подстроки "wow"

Пример:
s = "wowhatamanwowowpalehche"
...
> 3
"""


def find_letters(number, letters):
    triple = ''.join(letters)
    if triple == "wow":
        return number + 1
    else:
        return number


def task3(string):
    return reduce(find_letters, zip(string[0::1], string[1::1], string[2::1]), 0)


if __name__ == '__main__':
    a = "wowhatamanwowowpalehche"
    print task3(a)