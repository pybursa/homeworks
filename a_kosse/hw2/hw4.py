#!/usr/bin/env python
# -*- coding: utf-8 -*-

def chet_nechet(in_list):
    chet = len(in_list) % 2
    result = []
    for i in in_list:
        if i % 2 == chet:
            result.append(i)
    return result

if __name__ == "__main__":
    print chet_nechet([3,7,12])
    print chet_nechet([3,7,12,7])
