#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cort(data):
    result = []
    temp = []

    for i in data:
        if len(temp) == 2:
            result.append(tuple(temp))
            temp = []

        temp.append(i)

    if temp:
        result.append(tuple(temp))

    return tuple(result)

if __name__ == '__main__':
    print cort((1, 4, 8, 6, 3, 7, 1))
