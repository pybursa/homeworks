#!/usr/bin/env python
# -*- coding: utf-8 -*-


def separator(data):
    chet = []
    nechet = []

    for i in data:
        if i % 2 == 0:
            chet.append(i)
        else:
            nechet.append(i)

    nechet.sort()
    chet.sort()
    chet.reverse()

    return nechet + chet

if __name__ == '__main__':
    print separator([1, 4, 8, 6, 3, 7, 1])
