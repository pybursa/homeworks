#!/usr/bin/env python
# -*- coding: utf-8 -*-


def razver(data):
    result = []

    for i in data:
        if type(i) is not list:
            result.append(i)
            continue

        for v in i:
            result.append(v)

    return result

if __name__ == '__main__':
    print razver([[1], [4, 8], [6, 3, 7], [1, 3]])
