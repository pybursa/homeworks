# -*- coding: utf-8 -*-

"""
Задание 2: Симметрия.
УСЛОВИЕ:
Фрагмент кода, который принимает строку и определяет симметрична ли строка.
(Возвращает True или False).
Пример:
"abba" >> True
"arbat" >> False
"""

s1 = 'abba'
s2 = 'abcdedcba'
s3 = 'ghghghghgh'


def task2(x):
    x1 = x
    x2 = x[::-1]
    if x1 == x2:
        return True
    else:
        return False


if __name__ == '__main__':
    print task2(s1)
    print task2(s2)
    print task2(s3)