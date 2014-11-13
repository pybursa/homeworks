# coding=utf-8
"""
Задание 4: Чет-нечет.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и фильтрует его по четным (удаляет нечетные),
если количество элементов в списке является четным и наоборот
(удаляет четные, если элементов изначально нечетное количество).
Пример:
[3,7,12] >> [3,7]
[3,7,12,7] >> [12]
"""


def task04(input_data):
    # return_data = []
    # for element in input_data:
    #     if len(input_data) % 2 == element % 2:
    #         return_data.append(element)
    return [element for element in input_data if len(input_data) % 2 == element % 2]


if __name__ == '__main__':
    print task04([3, 7, 12])
    print task04([3, 7, 12, 7])

