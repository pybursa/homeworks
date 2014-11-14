#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maln'

# Return type name.
# @param <type> obj
def typer(obj):
    return type(obj).__name__

a = input(u"Введите первую переменную:")
b = input(u"Введите вторую переменную:")

print typer(a)
print typer(b)

if (typer(a) == 'str' or typer(a) == 'int') and (typer(b) == 'str' or typer(b) == 'int'):
    if typer(a) == 'str' or typer(b) == 'str':
        print u'Получена строка'
    else:
        if a > b:
            print u'Больше'
        elif  a < b:
            print u'Меньше'
        else:
            print u'Pавны'
else:
    print u'Ошибка ввода. Введите строки или цифры'
