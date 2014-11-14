# Author: Oleg Shestakov
# -*- coding: utf-8 -*-

# Задание 7: уникальный набор.
# УСЛОВИЕ:
# Реализовать функцию, которая принимает список елементов и убирает из него
# все дубликаты (формирует список уникальных элементов).
# Сделать вариант с сохранением порядка следования элементов и вариант,
# в кот. сортировка элементов не принципиальна.
# Пример:
# а) assert unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")]
# б) assert unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]
# TODO: I don't know how to sort result array.

def unique_ordered(arr):
    for i in arr:
        while arr.count(i) > 1:
            index = arr.index(i)
            remove_index = arr.index(i, index)
            arr.pop(remove_index)

    # print sorted(arr)
    print arr
    return arr


unique_ordered(["a", 5, 2, 5, (1, "a"), "a"])