#!/usr/bin/env python
# -*- coding: utf-8 -*-

string = raw_input('Введите строку: ')

print '1-й вариант:', string[::-1]

print '2-й вариант:', ''.join(reversed(string))

list = list(string)
list.reverse()
print '3-й вариант:', ''.join(list)

def rev(str):
  rev_str = ''
  l = len(str)
  
  for i in range(l):
    rev_str += str[l - i - 1]

  return rev_str

print '4-й вариант:', rev(string)
