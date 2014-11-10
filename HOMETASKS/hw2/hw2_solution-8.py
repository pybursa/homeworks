# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 8: Двууровневый кортеж. (бонусное)

УСЛОВИЕ:
Фрагмент кода, который принимает кортеж любых чисел и модифицирует его
в кортеж кортежей по два элемента (парами).

Пример:
(1,4,8,6,3,7,1) >> ((1,4),(8,6),(3,7),(1,))
"""


def double_tuple_1(T):
    result = []
    for i in range(0, len(T), 2):
        t = (T[i:i+2])
        result.append(t)
    return tuple(result)


def double_tuple_2(T):
    return tuple([T[i:i+2] for i, item in enumerate(T) if i % 2 == 0])


if __name__ == "__main__":
    print double_tuple_2((1,4,8,6,3,7,1))
    assert double_tuple_1((1,4,8,6,3,7,1)) == ((1,4),(8,6),(3,7),(1,))
    assert double_tuple_2((1,4,8,6,3,7,1)) == ((1,4),(8,6),(3,7),(1,))
