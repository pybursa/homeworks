# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 5: Сепаратор.

УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и модифицирует его следующим образом:
- в начале списка идут нечетные числа в порядке возрастания,
- далее идут четные числа в порядке убывания.

Пример:
[1,4,8,6,3,7,1] >> [1,1,3,7,8,6,4]
"""


def separ_1(L):
    evens = []
    for item in L:
        if item % 2 == 0:
            evens.append(item)
            L.remove(item)
    L.sort()
    evens.sort(reverse=True)
    L.extend(evens)
    return L


def separ_2(L):
    evens = []
    odds = []
    for item in sorted(L):
        evens.insert(0, item) if item % 2 == 0 else odds.append(item)
    return odds + evens


def separ_3(L):
    result = []
    for item in sorted(L, reverse=True):
        result.insert(0, item) if item % 2 == 1 else result.append(item)
    return result


def separ_4(L):
    odds = filter(lambda x: x % 2 == 1, L)
    evens = filter(lambda x: x % 2 == 0, L)
    return sorted(odds) + sorted(evens, reverse=True)


if __name__ == "__main__":
    assert separ_1([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]
    assert separ_2([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]
    assert separ_3([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]
    assert separ_4([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]
