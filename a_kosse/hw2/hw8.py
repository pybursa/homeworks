#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dva_urovna(in_tuple):
    lst = list(in_tuple)
    result = []
    for i in range(0,len(lst),2):
        if i+1 < len(lst):
            result.append((lst[i],lst[i+1]))
        else:
            result.append((lst[i],))
    r = tuple(result)
    return r


if __name__ == "__main__":

    print dva_urovna((1,4,8,6,3,7,1))
