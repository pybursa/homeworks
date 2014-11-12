# -*- coding: utf-8 -*-

"""
Задание 5: Псевдосумма.
УСЛОВИЕ:
Принимать любое натуральное число.
Выдавать сумму цифр, из которых число состоит.
Не использовать оператор "+" и встроенную функцию sum().
Пример:
456 >> 15
"""

n = 456


def pseudosum(input_number):
    iteration_symbol = 'x'
    calculating_list = []
    input_string = str(input_number)
    for i in input_string:
        calculating_list.append(iteration_symbol*int(i))
    psseudosum_string = ''.join(calculating_list)
    result = psseudosum_string.__len__()
    return result

if __name__ == '__main__':
    print pseudosum(n)