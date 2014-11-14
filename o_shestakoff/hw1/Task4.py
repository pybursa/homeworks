# Author: Oleg Shestakov
# -*- coding: utf-8 -*-

# Задание 4: упорядоченная подстрока.
# УСЛОВИЕ:
# Построить функционал который будет находить в строке подстроку максимальной длины,
# в которой буквы упорядочены в алфавитном порядке.
# ВХОД: строка
# ВЫХОД: подстрока
# Пример:
# s = "sabrrtuwacaddabra"
# ...
# > "abrrtuw"


s = "sabrrtuwacaddabra"

# string_arr = list(s)
result = list()

temp = list()

for i in s:
    if len(temp) == 0:
        temp.append(i)
    else:
        if ord(i) >= ord(temp[len(temp) - 1]):
            temp.append(i)
        else:
            result.insert(0, list(temp))
            temp = []
            temp.append(i)


def sortByLength(inputArr):
    return len(inputArr)


result.sort(key=sortByLength)

print "".join(result[len(result) - 1])