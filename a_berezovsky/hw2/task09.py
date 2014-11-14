# coding=utf-8
"""
Задание 9: Уплощение строптивого. (бонусное)
УСЛОВИЕ:
Фрагмент кода, который принимает список списков, и делает список "плоским" -
разворачивая элементы внутренних списков во вмещающий список.
Пример:
[[1],[4,8],[6,3,7],[1,3]] >> [1,4,8,6,3,7,1,3]
"""

def task09(input_data):
    return_data = []
    for element in input_data:
        if isinstance(element, list):
            return_data += task09(element)
        else:
            return_data.append(element)
    return return_data


if __name__ == '__main__':
    print task09([[1], [4, 8], [6, 3, 7], [1, 3]])

