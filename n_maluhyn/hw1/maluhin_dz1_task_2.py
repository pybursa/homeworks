# -*- coding: utf-8 -*-
# Подсчет вхождения в строку символов из перечня.
# @param str chars Перечень символов для поиска.  
# @param str text Строка для подстчета вхождений.
def countChars(chars, text):
    n = 0
    for char in text:
        if char in chars or char in chars.upper():
            n += 1
    return n

text = u"Текст для поиска гластных "
g = countChars(u"аеёиоуыэюя", text)

print u"гласных: %i" % (g)

