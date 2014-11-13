# -*- coding: utf-8 -*-
"""
Задание 4: упорядоченная подстрока.

УСЛОВИЕ:
Построить функционал который будет находить в строке подстроку максимальной длины,
в которой буквы упорядочены в алфавитном порядке.

ВХОД: строка
ВЫХОД: подстрока

Пример:
s = "sabrrtuwacaddabra"
...
> "abrrtuw"
"""


def task4(string):
    arr = []
    for string_index in xrange(0, len(string)):
        substring = string[string_index]
        for letter_index in xrange(string_index + 1, len(string)):
            if ord(string[string_index]) < ord(string[letter_index]):
                substring += string[letter_index]
            else:
                break
        arr.append(substring)
    return max(arr, key=len)


if __name__ == '__main__':
    a = "sabrrtuwacaddabra"
    print task4(a)