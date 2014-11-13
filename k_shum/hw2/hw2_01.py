#!/usr/bin/env python
# -*- coding: utf-8 -*-


def squares(data):
    result = [n*n for n in data]
    return result if type(data) == list else tuple(result)

if __name__ == '__main__':
    print squares([1, 2, 3])
    print squares((1, 2, 3))
