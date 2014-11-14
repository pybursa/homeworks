#!/usr/bin/env python
# -*- coding: utf-8 -*-


def chet(data):
    result = []
    for i in data:
        if i % 2 == 0:
            result.append(i)
    return result


def nechet(data):
    result = []
    for i in data:
        if i % 2 != 0:
            result.append(i)
    return result


def chetnechet(data):
    return chet(data) if len(data) % 2 == 0 else nechet(data)

if __name__ == '__main__':
    print chetnechet([3, 7, 12])
    print chetnechet([3, 7, 12, 7])
