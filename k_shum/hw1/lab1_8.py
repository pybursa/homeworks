#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')

print '1-й вариант:', t[2::3]

result = []
l = len(t)
i = 1

while i <= l:
  if not i % 3:
    result.append(t[i-1])
  i += 1
  
print '2-й вариант:', tuple(result)
