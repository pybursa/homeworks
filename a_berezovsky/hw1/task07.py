# -*- coding: utf-8 -*-
"""
Задание 7: уникальный набор.

УСЛОВИЕ:
Реализовать функцию, которая принимает список елементов и убирает из него все дубликаты
(формирует список уникальных элементов).
Сделать вариант с сохранением порядка следования элементов и вариант, в кот. сортировка элементов не принципиальна.

Пример:
а) assert unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")]
б) assert unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]
"""


def task7_unique_disordered(input_list):
    return list(set(input_list))


def task7_unique_ordered(input_list):
    return_list = []
    for element in input_list:
        if element not in return_list:
            return_list.append(element)
    return return_list


if __name__ == '__main__':
    print task7_unique_ordered(["a", 5, 2, 5, (1, "a"), "a"])
    print task7_unique_disordered(["a", 5, 2, 5, (1, "a"), "a"])