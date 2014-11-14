# -*- coding: utf-8 -*-

"""
Задание 1: Квадраты.
УСЛОВИЕ:
Фрагмент кода, который принимает набор (список, кортеж) чисел и возвращает набор
ТОГО ЖЕ типа со значениями квадратов этих чисел.
Пример:
[1,2,3] >> [1,4,9]
(1,2,3) >> (1,4,9)
"""

s1 = [1, 5, 18]
s2 = (1, 5, 18)


def squared(x):
    return x*x


def task1(x):
    if type(x) is list:
        return map(squared, x)
    elif type(x) is tuple:
        return tuple(map(squared, x))

if __name__ == '__main__':
    print task1(s1)
    print task1(s2)