#!/usr/bin/env python
# -*- coding: utf-8 -*-


def easy_num(start, end):
    result = []
    temp = 0

    for i in xrange(start, end):
        for j in xrange(2, i):
            if i % j == 0:
                temp += 1

        if temp == 0:
            result.append(i)
        else:
            temp = 0

    return result

if __name__ == '__main__':
    print easy_num(2, 10000)
