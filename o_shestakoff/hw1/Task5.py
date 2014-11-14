# Author: Oleg Shestakov
# -*- coding: utf-8 -*-

# Задание 5: определение типа.
# УСЛОВИЕ:
# функция, которая принимает объект и выводит строку с наименованием типа этого объекта.
# Пример:
# typer(666) == "int"
# typer("666") == "str"
# typer(typer) == "function"

import types


def typer(typeObj):
    if type(typeObj) is types.IntType:
        return "int"
    elif type(typeObj) is types.StringType:
        return "str"
    elif type(typeObj) is types.FunctionType:
        return "function"
    pass


print typer(666)
print typer('666')
print typer(typer)