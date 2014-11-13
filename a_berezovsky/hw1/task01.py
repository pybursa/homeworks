# -*- coding: utf-8 -*-
"""
Задание 1: реверс строки.

УСЛОВИЕ:
Преобразовать строку "ecnalubma" в ее зеркальное отражение (реверсировать).
Сделать это четырьмя разными способами.

ВХОД: строка
ВЫХОД: реверсированная строка

Пример:
a = "ambulance"
...
print result
> "ecnalubma"
"""
from collections import deque


def task1_1(string):
    return string[::-1]


def task1_2(string):
    arr = list(string)
    arr.reverse()
    return "".join(arr)


def task1_3(string):
    arr = []
    return_string = ""
    for letter in string:
        arr.append(letter)
    while len(arr) != 0:
        return_string += arr.pop()
    return return_string


def task1_4(string):
    arr = deque()
    arr.extendleft(string)
    return "".join(arr)


if __name__ == "__main__":
    a = "ambulance"
    print task1_1(a)
    print task1_2(a)
    print task1_3(a)
    print task1_4(a)