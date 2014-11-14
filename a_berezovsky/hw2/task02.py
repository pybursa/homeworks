# coding=utf-8
"""
Задание 2: Симметрия.
УСЛОВИЕ:
Фрагмент кода, который принимает строку и определяет симметрична ли строка.
(Возвращает True или False).
Пример:
"abba" >> True
"arbat" >> False
"""


def task02(input_data):
    return input_data == input_data[::-1]


if __name__ == '__main__':
    print task02("abba")
    print task02("arbat")

