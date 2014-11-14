#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check(a, b):
  if type(a) is str or type(b) is str:
    return 'получена строка'
  
  if a > b:
    return 'больше'

  if a < b:
    return 'меньше'

  return 'равны'

print check(1, '1')
print check(1, 1)
print check(2, 1)
print check(1, 2)
