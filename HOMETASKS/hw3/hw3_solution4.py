#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание 4: Imports.

УСЛОВИЕ:
Произвести импортирование модулей стандартной библиотеки Python: "os" и "sys".
Вывести справку по всем функциям каждого модуля.
"""

__author__ = 'wowkalucky'


import sys
import os


def show_guts(module):
    """Prints module objects docstrings"""

    def sep_line(sep="=", n=70):
        print sep * n

    sep_line()
    print "DOCSTRINGS OF '%s' MODULE\n\n" % module.__name__
    for obj_name in dir(module):
        if not obj_name.startswith("_"):
            print obj_name
            sep_line(".")
            print eval("{module_name}.{object_name}.__doc__".format(**{"module_name": module.__name__,
                                                                        "object_name": obj_name}))
            sep_line()


if __name__ == "__main__":
    show_guts(sys)
    show_guts(os)
