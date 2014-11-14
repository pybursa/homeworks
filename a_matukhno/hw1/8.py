# -*- coding: utf-8 -*-

input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')


def each_third(input_tuple):
    copy = []
    res = [x for x in xrange(2, input_tuple.__len__()-1, 3)]
    for i in res:
        copy.append(input_tuple[i])
    result = tuple(j for j in copy)
    return result



print each_third(input_tuple)