# -*- coding: utf8 -*-

u"""
содержит вспомогательный класс обработки персональных данных и функциюнкцию которая
перезаписывает файл с исходными персональными данными
"""


__author__ = "kuzin.valeriy"
__email__ = "kuzin.valeriy@gmail.com"
__date__ = "2014-11-21"


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

def modifier(data_file):
    u'''чтение файла .csv, перезапись файла с новыми столбцами'''
    all_data = []
    with open(data_file, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            if 'id' in row and 'surname' in row:
                row.insert(3, 'fullname')
                row.append('age')
            else:
                row_data = Person(row[1], row[2], row[3], row[4])
                data_age = row_data.get_age()
                data_fullname = row_data.get_fullname()
                row.insert(3, data_fullname)
                row.append(data_age)
            all_data.append(row)
    fd.close()

    writer = csv.writer(open(data_file, 'w'))
    writer.writerows(all_data)

