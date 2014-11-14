# -*- coding: utf-8 -*-
"""
Задание 3: Триделение.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и возвращает словарь вида:
{число: boolean}, где: boolean - True или False в зависимости делится ли число на 3
без остатка.
Пример:
[3,7,12] >> {3:True, 12:True, 7:False}
"""

s = [3, 7, 12]


def task3(x):
    result = {}
    for el in s:
        if el % 3 == 0:
            result[el] = True
        else:
            result[el] = False
    return result


if __name__ == '__main__':
    print task3(s)
