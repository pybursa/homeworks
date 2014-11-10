# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 9: Уплощение строптивого. (бонусное)

УСЛОВИЕ:
Фрагмент кода, который принимает список списков, и делает список "плоским" -
разворачивая элементы внутренних списков во вмещающий список.

Пример:
[[1],[4,8],[6,3,7],[1,3]] >> [1,4,8,6,3,7,1,3]
"""


def flatter_1(L):
    result = []
    for list_item in L:
        for item in list_item:
            result.append(item)
    return result


def flatter_2(L):
    for list_item in L[:]:
        L.remove(list_item)
        L.extend(list_item)
    return L


def flatter_3(L):
    return [item for list_item in L for item in list_item]


if __name__ == "__main__":
    assert flatter_1([[1],[4,8],[6,3,7],[1,3]]) == [1,4,8,6,3,7,1,3]
    assert flatter_2([[1],[4,8],[6,3,7],[1,3]]) == [1,4,8,6,3,7,1,3]
    assert flatter_3([[1],[4,8],[6,3,7],[1,3]]) == [1,4,8,6,3,7,1,3]


