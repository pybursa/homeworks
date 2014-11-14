# Author: Oleg Shestakov
# -*- coding: utf-8 -*-
# Задание 1: реверс строки.
# УСЛОВИЕ:
# Преобразовать строку "ecnalubma" в ее зеркальное отражение (реверсировать).
# Сделать это четырьмя разными способами.
# ВХОД: строка
# ВЫХОД: реверсированная строка
# Пример:
# a = "ambulance"
# ...
# print result
# > "ecnalubma"

s = "ecnalubma"

# First method
temp = list(s)

temp.reverse()

temp = "".join(temp)

print temp

# Second method
temp = []

for i in range(1, len(s) + 1):
    temp.append(s[-i])

print "".join(temp)

# Third method

temp = []

for i in range(len(s) - 1, -1, -1):
    temp.append(s[i])

print "".join(temp)

# Fourth method

temp = []

for i in s:
    temp.insert(0, i)

print "".join(temp)