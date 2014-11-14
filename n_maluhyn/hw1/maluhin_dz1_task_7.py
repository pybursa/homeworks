#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maln'

# Return list of unique. Order preserving.
# @param list seq
def unique_ordered(seq):
    output = []
    for x in seq:
        if x not in output:
            output.append(x)
    return output

# Return list of unique. Order not preserving.
#param list seq
def unique_disordered(seq):
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()

print unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) # == ["a", 5, 2, (1, "a")]

print unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) # [2, "a", 5, (1, "a")]
