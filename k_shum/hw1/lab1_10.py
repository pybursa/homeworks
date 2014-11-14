#!/usr/bin/env python
# -*- coding: utf-8 -*-

glas = ['a', 'e', 'i', 'o', 'u']

while True:
  string = raw_input('Please, enter your string: ').lower()

  count = 0

  for i in string:
    if i in glas:
      count += 1

  if count:
    print 'The string contains', count, 'vowels'
  else:
    print "The string doesn't contain vowels"

  cont = raw_input('Continue? (yes/no) ')

  while cont != 'yes' and cont != 'no':
    cont = raw_input('Please, enter corrent answer. Continue? (yes/no) ')
    
  if cont == 'yes':
    print 'Hurray!'
  else:
    print 'It was nice to count your vowels!'
    break
