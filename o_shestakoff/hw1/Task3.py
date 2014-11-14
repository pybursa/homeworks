# Author: Oleg Shestakov
# -*- coding: utf-8 -*-

# Задание 3: подстчет вхождений подстроки.
# УСЛОВИЕ:
# Реализовать подсчеы количества вхождений подстроки "wow" в строке.
# ВХОД: строка
# ВЫХОД: число вхождений подстроки "wow"
# Пример:
# s = "wowhatamanwowowpalehche"
# ...
# > 3

s = "wowhatamanwowowpalehche"

start = 0
stop = len(s)
pos = -1
count = 0

while s.find('wow', start, stop) != -1:
    if pos != s.find('wow', start, stop):
        pos = s.find('wow', start, stop)
        count += 1
        start = pos + 2

print count