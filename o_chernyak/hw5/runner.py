# -*- coding: utf-8 -*-

u"""
Скрипт запуска ДЗ.
"""

__author__ = "o_chernyak"
__email__ = "olgache73@gmail.com"
__date__ = "2014-11-20"

from hw5_task1 import Person
from hw5_tests import tests_for_hw5

def runner():
    u"""Запускает выполнение всех задач"""
    petrov = Person("Petrov", "Peter", "1979-11-30")
    petrov.get_fullname()
    petrov.get_age()

    sidorov = Person("Sidorov", "Sid", "1977-01-17", "Sider")
    sidorov.get_fullname()
    sidorov.get_age()    

if __name__ == '__main__':
    runner()
   
