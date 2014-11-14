# coding=utf-8
from math import sqrt


def task06():
    """
    Задание 6: Простые числа. (бонусное)

    УСЛОВИЕ:
    Вывести на печать 10000 первых натуральных простых чисел.
    Напомню, что это те, которые делятся без остатка не себя и 1, начиная с числа 2.
    """
    for number in xrange(1, 10000 + 1):
        for multiple in xrange(2, int(sqrt(number) + 1)):
            if number % multiple == 0:
                break
        else:
            print number


if __name__ == '__main__':
    task06()

