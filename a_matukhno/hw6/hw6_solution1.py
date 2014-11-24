#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
УСЛОВИЕ:
дан файл с данными: homeworks/HOMETASKS/hw6/data.csv

Написать функцию modifier(filename), которая должна:
- вычитать данные;
- создать объекты класса Person на основании полученных данных;
- модифицировать данные:
 а) добавить графу полного имени (fullname) после графы с именем (name)
 б) добавить графу с возрастом (age) в конец.

На выходе получить файл, расширенный указанным образом.
"""

__author__ = 'Andrey Matukhno'

import csv
import datetime


class Person(object):
    def __init__(self, surname, first_name,
                 birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        if nickname is not None:
            self.nickname = nickname
        self.birth_date = datetime.date(int(birth_date[:4]),
                                        int(birth_date[5:7]),
                                        int(birth_date[8:]))

    def get_age(self):
        age = datetime.date.today().year - self.birth_date.year
        return str(age)

    def get_fullname(self):
        fullname = self.surname + ' ' + self.first_name
        return fullname


def modifier(file_name):
    new_rows = []
    with open(file_name, 'r+') as csv_file:
        data_read = csv.reader(csv_file)
        for row in data_read:
            new_row = row
            if new_row[0] == 'id':
                new_row.insert(3, 'fullname')
                new_row.append('age')
            else:
                if new_row[4]:
                    contact = Person(new_row[1], new_row[2],
                                     new_row[3], new_row[4])
                else:
                    contact = Person(new_row[1],
                                     new_row[2], new_row[3])

                new_row.insert(3, contact.get_fullname())
                new_row.append(contact.get_age())
            new_rows.append(new_row)

    with open(file_name, 'wb') as csv_file:
        data_write = csv.writer(csv_file)
        data_write.writerows(new_rows)