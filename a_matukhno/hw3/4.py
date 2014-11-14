# -*- coding: utf-8 -*-

"""
Задание 4: Imports.
УСЛОВИЕ:
Произвести импортирование модулей стандартной библиотеки Python: "os" и "sys".
Вывести справку по всем функциям каждого модуля.
"""

import os
import sys

print '=== os module ==='
print dir(os)
for func in dir(os):
    print help(func)
print '='*100
print '=== sys module ==='
print dir(sys)
for func in dir(sys):
    print help(func)
print '='*100

