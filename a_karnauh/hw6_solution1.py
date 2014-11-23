# -*- coding: utf8 -*-

u"""Задание 6.1"""

__author__ = "anna-karnaukh"
__email__ = "anna.karnaukh1@gmail.com"
__date__ = "2014-11-23"


import sys
import csv
from hw5_solution1 import Person


def modifier(filename):
    u"""Функция получает название файла и изменяет его согласно условию."""
    with open(filename) as csvfile:
        data = csv.reader(csvfile)
        header = data.next()
        persons = []
        for row in data:
            person = Person(*row[1:])
            persons.append(person)
        header.insert(3, "fullname")
        header.append("age")
        
    with open(filename, "w") as csvfile:
        data = csv.writer(csvfile)
        data.writerow(header)
        count = 1
        for item in persons:
            data.writerow([count, item.surname, item.first_name, 
                item.get_fullname(), item.birth_date, item.nickname, 
                item.get_age()])
            count = count + 1
