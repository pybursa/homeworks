# -*- coding: utf-8 -*-
"""
Задание 8: каждый третий.

УСЛОВИЕ:
Реализовать функционал который принимает кортеж и возвращает прореженный кортеж, оставляя только каждый третий элемент.
Реализовать задачу двумя разными вариантами.

Пример:
t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
...
> (3,6,9,'b')
"""


def task8_1(elements):
    return_tuple = []
    i = 0
    for element in elements:
        if i == 2:
            return_tuple.append(element)
            i = 0
        else:
            i += 1
    return tuple(return_tuple)


def task8_2(elements):
    return tuple([element for element in elements[2::3]])


if __name__ == '__main__':
    print task8_1((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c'))
    print task8_2((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c'))