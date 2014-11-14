#!/usr/bin/env python
# -*- coding: utf-8 -*-

def square(incom):
    list_out = []
    for i in incom:
        list_out.append(i*i)
    if isinstance(incom, tuple):
        return tuple(list_out)
    else:
        return list_out


if __name__ == "__main__":
    print square([1,2,3])
    print square((1,2,3))


