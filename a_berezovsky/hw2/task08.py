# coding=utf-8
"""
Задание 8: Двууровневый кортеж. (бонусное)
УСЛОВИЕ:
Фрагмент кода, который принимает кортеж любых чисел и модифицирует его
в кортеж кортежей по два элемента (парами).
Пример:
(1,4,8,6,3,7,1) >> ((1,4),(8,6),(3,7),(1,))
"""


def task08(input_data):
    return_data = []
    for index in xrange(0, len(input_data), 2):
        try:
            return_data.append((input_data[index], input_data[index + 1]))
        except IndexError:
            return_data.append((input_data[index],))
    return tuple(return_data)


if __name__ == '__main__':
    print task08((1, 4, 8, 6, 3, 7, 1))

