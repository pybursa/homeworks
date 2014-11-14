# Author: Oleg Shestakov
# -*- coding: utf-8 -*-

# Задание 6: А & B.
# УСЛОВИЕ:
# Написать фрагмент python кода, который будет анализировать две переменные (А и В),
# которые могут быть типа "str" или "int".
# В зависимости от значения переменных код должен выводить на печать ОДНО из следующих сообщений:
# - "получена строка" - если хотя бы одна из переменных является строкой;
# - "больше" - если А больше В;
# - "равны" - если значения переменных равны;
# - "меньше" - если А меньше В.

import types


def typer(typeObj):
    if type(typeObj) is types.IntType:
        return "int"
    elif type(typeObj) is types.StringType:
        return "str"
    elif type(typeObj) is types.FunctionType:
        return "function"
    pass


def comparator(value1, value2):
    if typer(value1) == 'str' or typer(value2) == 'str':
        return "string"
    else:
        if value1 > value2:
            return "a is greater than b"
        elif value1 < value2:
            return "a is less than b"
        else:
            return "a and b are equal"


print comparator(1, 2)
print comparator(2, 1)
print comparator('s', 1)
print comparator(1, 's')