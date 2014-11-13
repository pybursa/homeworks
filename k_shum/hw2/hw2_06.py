#!/usr/bin/env python
# -*- coding: utf-8 -*-


def classificator(data):
    result = {}

    for k, v in data.items():
        t = type(v).__name__
        if t not in result:
            result[t] = 0
        result[t] += 1

    return result

if __name__ == '__main__':
    print classificator({'a': 1, 3: [1, 5], 'e': 'abc', '6': []})
