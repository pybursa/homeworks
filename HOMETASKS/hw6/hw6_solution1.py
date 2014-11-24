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
"""

__author__ = "wowkalucky"
__email__ = "wowkalucky@gmail.com"
__date__ = "2014-11-20"


import csv
import os
from datetime import datetime, date


class Person(object):
    """Represents notebook entry"""
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format = "%Y-%m-%d"
            datetime_object = datetime.strptime(birthdate, date_format)
            self.birth_date = datetime_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days // 365.25))

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self. first_name)



def modifier(file_name):
    """Reads and modifies input csv file"""
    with open(file_name, 'r') as fr:
        reader_dict = csv.DictReader(fr)
        with open('temp', 'w') as fw:
            titles = reader_dict.fieldnames[:]
            titles.insert(3, 'fullname')
            titles.append('age')
            writer_dict = csv.DictWriter(fw, fieldnames=titles)
            writer_dict.writeheader()
            for row_dict in reader_dict:
                surname = row_dict['surname']
                name = row_dict['name']
                birthdate = row_dict['birthdate']
                nickname = row_dict['nickname'] or None
                person = Person(surname, name, birthdate, nickname)
                row_dict['fullname'] = person.get_fullname()
                row_dict['age'] = person.get_age()
                writer_dict.writerow(row_dict)
    os.rename('temp', file_name)
