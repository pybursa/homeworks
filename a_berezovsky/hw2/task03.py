# coding=utf-8
"""
Задание 3: Триделение.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и возвращает словарь вида:
{число: boolean}, где: boolean - True или False в зависимости делится ли число на 3
без остатка.
Пример:
[3,7,12] >> {3:True, 12:True, 7:False}
"""


def task03(input_data):
    # return_data = {}
    # for element in input_data:
    #     return_data[element] = element % 3 == 0
    # return return_data
    return dict([(element, element % 3 == 0) for element in input_data])


if __name__ == '__main__':
    print task03([3, 7, 12])

