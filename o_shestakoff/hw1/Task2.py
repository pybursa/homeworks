# Author: Oleg Shestakov
# -*- coding: utf-8 -*-

# Задание 2: подсчет гласных.
# УСЛОВИЕ:
# подсчет гласных букв в строке.
# Примечание:
# - для простоты на вход принимаем строку из букв латинского алфавита;
# - набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
# - программа должна быть нечувствительна к регистру.
# Пример:
# s = "hApPyHalLOweEn!"
# ...
# print result
# > 5

s = "hApPyHalLOweEn!"


def switch_case(case):
    return {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True
    }.get(case, False)


count = 0

temp = s.lower()

for i in temp:
    if switch_case(i):
        count += 1

print count