# coding=utf-8
"""
Задание 1: Квадраты.
УСЛОВИЕ:
Фрагмент кода, который принимает набор (список, кортеж) чисел и возвращает набор
ТОГО ЖЕ типа со значениями квадратов этих чисел.
Пример:
[1,2,3] >> [1,4,9]
(1,2,3) >> (1,4,9)
"""


def task01(input_data):
    #squares = [element ** 2 for element in input_data]
    #return input_data.__class__(squares)
    return input_data.__class__([element ** 2 for element in input_data])


if __name__ == '__main__':
    print task01([1, 2, 3])
    print task01((1, 2, 3))

