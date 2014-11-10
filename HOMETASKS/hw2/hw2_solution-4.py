# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 4: Чет-нечет.

УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и фильтрует его по четным (удаляет нечетные),
если количество элементов в списке является четным и наоборот (удаляет четные, если элементов изначально нечетное количество).

Пример:
[3,7,12] >> [3,7]
[3,7,12,7] >> [12]
"""


def evenodd_1(L):
    is_even = len(L) % 2 == 0
    result = []
    for item in L:
        if is_even and item % 2 == 0:
            result.append(item)
        elif not is_even and item % 2 == 1:
            result.append(item)
    return result


def evenodd_2(L):
    is_even = len(L) % 2 == 0
    evens = []
    for i, item in enumerate(L):
        if item % 2 == 0:
            evens.append(L.pop(i))
    return evens if is_even else L


def evenodd_3(L):
    return [item for item in L if len(L) % 2 == item % 2]


if __name__ == "__main__":
    assert evenodd_1([3, 7, 12]) == [3,7]
    assert evenodd_1([3, 7, 12, 7]) == [12]
    assert evenodd_2([3, 7, 12]) == [3, 7]
    assert evenodd_2([3, 7, 12, 7]) == [12]
    assert evenodd_3([3, 7, 12]) == [3, 7]
    assert evenodd_3([3, 7, 12, 7]) == [12]
