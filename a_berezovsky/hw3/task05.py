# coding=utf-8
from operator import add


def task05(number):
    """
    Задание 5: Псевдосумма.

    УСЛОВИЕ:
    Принимать любое натуральное число.
    Выдавать сумму цифр, из которых число состоит.
    Не использовать оператор "+" и встроенную функцию sum().

    Пример:
    456 >> 15
    """
    digit_sum = 0
    for digit in list(str(number)):
        digit_sum = add(digit_sum, int(digit))
    return digit_sum

    # return reduce(lambda digit_sum, digit: add(digit_sum, int(digit)), list(str(number)), 0)

if __name__ == '__main__':
    print task05(456)

