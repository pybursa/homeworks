# -*- coding: utf8 -*-

u"""
Задание 1: вычитка по полной.

УСЛОВИЕ:
дан файл с данными: homeworks/HOMETASKS/hw6/data.csv

Написать функцию modifier(filename), которая должна:
- вычитать данные;
- создать объекты класса Person на основании полученных данных;
- модифицировать данные:
 а) добавить графу полного имени (fullname) после графы с именем (name)
 б) добавить графу с возрастом (age) в конец.

На выходе получить файл, расширенный указанным образом.

Примечание:
1) смотрите документацию по модулю csv;
(https://docs.python.org/2/library/csv.html?highlight=csv#module-csv)


Пример:

при запуске скрипта (homeworks/.../hw6/hw6_starter.py)

Тестов в этом задании не предусмотрено.

==============================================================================
"""

__author__ = "a_kushnaryoff"
__date__ = "2014-11-14"

import csv
from datetime import datetime


class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

        if type(nickname) is str and len(nickname) > 0:
            self.nickname = nickname

    def get_fullname(self):
        return self.surname + " " + self.first_name

    def get_age(self):
        return str(int((datetime.now().date() - self.birth_date).
                       days / 365.25))


def modifier(file_name):
    array_args = []

    with open(file_name, 'r') as fp:
        csv_r = csv.reader(fp)
        for row in csv_r:
            array_args.append(row)

        for row_num, list_row in enumerate(array_args):
            if row_num == 0:
                list_row.append('age')
                list_row.insert(3, 'fullname')
            else:
                person = Person(*list_row[1::])
                list_row.append(person.get_age())
                list_row.insert(3, person.get_fullname())
                if '' in list_row:
                    list_row.remove('')

        with open(file_name, 'w') as wp:
            csv_wr = csv.writer(wp)
            for row in array_args:
                csv_wr.writerow(row)
