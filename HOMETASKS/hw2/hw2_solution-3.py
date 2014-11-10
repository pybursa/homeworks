# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 3: Триделение.

УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и возвращает словарь вида:
{число: boolean}, где: boolean - True или False в зависимости делится ли число на 3
без остатка.

Пример:
[3,7,12] >> {3:True, 12:True, 7:False}
"""


def triples_1(L):
    result = {}
    for item in L:
        result[item] = item % 3 == 0
    return result


def triples_2(L):
    return dict((item, (item % 3 == 0)) for item in L)


if __name__ == "__main__":
    assert triples_1([3, 7, 12]) == {3: True, 12: True, 7: False}
    assert triples_1([9, 1, 2, 5, 9, 33]) == {1: False, 2: False, 5: False, 9: True, 33: True}
    assert triples_2([3, 7, 12]) == {3: True, 12: True, 7: False}
    assert triples_2([9, 1, 2, 5, 9, 33]) == {1: False, 2: False, 5: False, 9: True, 33: True}
