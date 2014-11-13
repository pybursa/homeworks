#!/usr/bin/env python
# -*- coding: utf-8 -*-


def psum(data):
    result = 0

    for i in str(data):
        result -= int(i)

    return abs(result)

if __name__ == '__main__':
    print psum(456)
