#!/usr/bin/env python
# -*- coding: utf-8 -*-

glas = ['a', 'e', 'i', 'o', 'u']

string = raw_input('Введите строку: ')

count = 0

for i in string:
  if i in glas:
    count += 1
    
print count
