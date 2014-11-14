#!/usr/bin/env python
# -*- coding: utf-8 -*-

string = raw_input('Введите строку: ')

result = ''
temp = ''
i = 0
l = len(string)

while l > i:
  temp += string[i]

  if len(temp) > len(result):
    result = temp

  if l != i+1 and string[i] > string[i+1]:
    temp = ''

  i += 1

print result
