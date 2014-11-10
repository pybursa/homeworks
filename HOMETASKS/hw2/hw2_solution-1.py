# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 1: Квадраты.

УСЛОВИЕ:
Фрагмент кода, который принимает набор (список, кортеж) чисел и возвращает набор
ТОГО ЖЕ типа со значениями квадратов этих чисел.

Пример:
[1,2,3] >> [1,4,9]
(1,2,3) >> (1,4,9)
"""


def squares_1(L):
    assert type(L) in [tuple, list]
    type_name = type(L)
    result = []
    for item in L:
        result.append(item * item)
    return type_name(result)


def squares_2(L):
    type_name = type(L)
    return type_name([item ** 2 for item in L])


def squares_3(L):
    return type(L)(map(lambda x: x**2, L))


if __name__ == "__main__":
    assert squares_1([1,2,3]) == [1, 4, 9]
    assert squares_1((1,2,3)) == (1, 4, 9)
    assert squares_2([1, 2, 3]) == [1, 4, 9]
    assert squares_2((1, 2, 3)) == (1, 4, 9)
    assert squares_3((1, 2, 3)) == [1, 4, 9]
    assert squares_3([1, 2, 3]) == (1, 4, 9)
