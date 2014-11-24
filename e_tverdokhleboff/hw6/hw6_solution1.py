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
"""

__author__ = "tverdokhlebov"
__email__ = "evgenij04@mail.ru"
__date__ = "2014-11-23"


from datetime import datetime, date
import csv

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
    mod_rows = []
    with open(file_name, 'rb') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            mod_row = row
            if mod_row[0] == 'id':
                mod_row.insert(3, 'fullname')
                mod_row.append('age')
            else:
                if mod_row[4]:
                    pers_inf = Person(mod_row[1], mod_row[2], mod_row[3], mod_row[4])
                else:
                    pers_inf = Person(mod_row[1], mod_row[2], mod_row[3])
 
                mod_row.insert(3, pers_inf.get_fullname())
                mod_row.append(pers_inf.get_age())
            mod_rows.append(mod_row)

    with open(file_name, 'wb') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerows(mod_rows)



