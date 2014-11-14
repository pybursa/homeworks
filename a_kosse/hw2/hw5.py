#!/usr/bin/env python
# -*- coding: utf-8 -*-

def separator(in_list):
    chet_list = []
    nechet_list = []
    for i in in_list:
        if i % 2 == 0:
            chet_list.append(i)
        else:
            nechet_list.append(i)
        chet_list.sort()
        chet_list.reverse()
        nechet_list.sort()
    return nechet_list + chet_list

if __name__ == "__main__":
    print separator([1,4,8,6,3,7,1])

