# coding=utf-8
def task04():
    """
    Задание 4: Imports.

    УСЛОВИЕ:
    Произвести импортирование модулей стандартной библиотеки Python: "os" и "sys".
    Вывести справку по всем функциям каждого модуля.
    """
    import os
    import sys

    for lib in (os, sys):
        for function in dir(lib):
            print help(function)


if __name__ == '__main__':
    task04()

