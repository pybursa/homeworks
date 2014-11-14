#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Я знаю что это не то, что вы хотели увидеть, но лекцию я проболел, так что решаю поставленную задачу как могу.
n = input('Enter number: ')
n = int(n)
total = 0
while n > 0:
    total -= ((n % 10) * -1)
    n //= 10
print('Sum  =', total)
