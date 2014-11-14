#!/usr/bin/env python
# -*- coding: utf-8 -*-
def simmetria(in_str):
    result = True
    for i in range(len(in_str)):
        if in_str[i] != in_str[-i-1]:
            result = False
    return result


if __name__ == "__main__":
    print simmetria('abba')
    print simmetria('arbat')

