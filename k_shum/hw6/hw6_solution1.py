# -*- coding: utf-8 -*-

u"""
Набор методов для ДЗ №6
"""

__author__ = "k.shym"
__email__ = "ks.shym@gmail.com"
__date__ = "2014-11-21"


import sys
import csv

sys.path.insert(0, '../hw5')
from hw5_solution1 import Person


def modifier(filename):
    u"""Получает строку c адресом файла и изменяет согласно условиям задачи."""
    with open(filename, 'r') as csvfile:
        data = []
        index_fullname = 0

        for i in csv.reader(csvfile):
            if not i[0].isdigit():
                index_fullname = i.index('name') + 1
                i.insert(index_fullname, 'fullname')
                i.append('age')
            else:
                p = Person(*i[1:])
                i.insert(index_fullname, p.get_fullname())
                i.append(p.get_age())
            data.append(i)

    with open(filename, 'w') as csvfile:
        wdata = csv.writer(csvfile)
        wdata.writerows(data)
