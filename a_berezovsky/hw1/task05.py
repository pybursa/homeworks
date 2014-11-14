# -*- coding: utf-8 -*-
"""
Задание 5: определение типа.

УСЛОВИЕ:
функция, которая принимает объект и выводит строку с наименованием типа этого объекта.

Пример:
typer(666) == "int"
typer("666") == "str"
typer(typer) == "function"
"""


def typer(variable):
    return type(variable).__name__


if __name__ == '__main__':
    print "666 type is %s" % typer(666)
    print "\"666\" type is %s" % typer("666")
    print "task5 type is %s" % typer(typer)