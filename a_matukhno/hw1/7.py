# -*- coding: utf-8 -*-
import random, math

input_list = [1, 2, 3, 'a', ('a', 'b'), 'a', 3, 2, 1]


def remove_dubs_ordered(entered_list):
    result = []
    for i in entered_list:
        if result.count(i) == 0:
            result.append(i)
    return result


def remove_dubs_disordered(entered_list):
    result = []
    while entered_list.__len__() > 0:
        i = entered_list.pop(random.randint(0, entered_list.__len__()-1))
        if result.count(i) == 0:
            result.append(i)
    return result



print remove_dubs_ordered(input_list)
print remove_dubs_disordered(input_list)