#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание 5: Псевдосумма.

УСЛОВИЕ:
Принимать любое натуральное число.
Выдавать сумму цифр, из которых число состоит.
Не использовать оператор "+" и встроенную функцию sum().

Пример:
456 >> 15
"""

__author__ = 'wowkalucky'


def pseudosum(num):
    base_list = [0]
    base_list.extend(list(str(num)))
    return abs(reduce(lambda x, y: x - int(y), base_list))


if __name__ == "__main__":
    assert pseudosum(456) == 15
    assert pseudosum(123321) == 12
