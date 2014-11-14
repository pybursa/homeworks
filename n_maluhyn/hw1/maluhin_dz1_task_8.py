#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maln'


# Perform uber-decimacia.
# @param cortege seq
def decimacia_1(seq):
    return seq[::3]


# Decimacia 2.
# @param cortege seq
def decimacia_2(seq):
    out_seq = []
    count = 0
    for i in seq:
        if count % 3 == 0:
            out_seq.append(i)
        count = count + 1
    return out_seq

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
print decimacia_1(t)
print decimacia_2(t)


