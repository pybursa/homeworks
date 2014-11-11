# -*- coding: utf-8 -*-
"""
Задание 2: подсчет гласных.

УСЛОВИЕ:
подсчет гласных букв в строке.

Примечание:
- для простоты на вход принимаем строку из букв латинского алфавита;
- набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
- программа должна быть нечувствительна к регистру.

Пример:
s = "hApPyHalLOweEn!"
...
print result
> 5
"""
import sys


def task2(string):
    return reduce(lambda number, letter: number + 1 if letter in ['a', 'e', 'i', 'o', 'u'] else number,
                  string.lower(), 0)


if __name__ == "__main__":
    a = "hApPyHalLOweEn!"
    print task2(a)
    print sys.argv