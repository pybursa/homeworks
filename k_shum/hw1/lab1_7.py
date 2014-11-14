#!/usr/bin/env python
# -*- coding: utf-8 -*-

def unique(l, ordered = False):
  if not ordered:
    return list(set(l))
  
  result = []
  for i in l:
    if i not in result:
      result.append(i)
  
  return result

print unique(["a", 5, 2, 5, (1, "a"), "a"], True)
print unique(["a", 5, 2, 5, (1, "a"), "a"])
