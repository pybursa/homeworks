#!/usr/bin/env python
# -*- coding: utf-8 -*-


def division(data):
    result = {}

    for i in data:
        result[i] = True if i % 3 == 0 else False

    return result

if __name__ == '__main__':
    print division([3, 7, 12])
