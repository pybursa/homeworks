# -*- coding: utf8 -*-

__autor__ = "Viktorov Eugene"
__email__ = "jekafromua@gmail.com"
__date__ = "2014-11-23"


import pprint
import csv
from datetime import datetime, date



class Person(object):
    """Represents notebook entry"""
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        if nickname is not None:
            self.nickname = nickname
        try:
            date_fromat = "%Y-%m-%d"
            datetime_object = datetime.strptime(birthdate, date_fromat)
            self.birth_date = datetime_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format"
                             "(YYYY-MM-DD)!")

    def get_age(self):
        today_date = datetime.today()
        age = [0, 0, 0]
        age[0] = today_date.year - self.birth_date.year
        age[1] = today_date.month - self.birth_date.month
        age[2] = today_date.day - self.birth_date.day
        if age[0] < 0:
            print 'Sorry, this day is yet to come)'
            return None
        for i in age:
            if i < 0:
                return age[0] - 1
        return age[0]

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self.first_name)



def modifer(filename):
    filename = 'data.csv'
    data_ = open(filename, 'r')
    table = [row for row in csv.reader(data_)]
    data_.close()
    outfile = open(filename, 'w')
    writer = csv.writer(outfile)
    writer.writerow(['id', 'surname', 'name',
                     'fullname', 'birthdate',
                     'nickname', 'age'
                   ])
    mod_string = []
    for r in range(1, len(table)):
        mod_string = table[r][1:]
        a = mod_string[0]
        b = mod_string[1]
        c = mod_string[2]
        d = mod_string[3]
        person = Person(a, b, c, d)
        mod_string.insert(3, person.get_fullname())
        mod_string.insert(6,person.get_age())
        mod_string.insert(0, r)
        writer.writerow(mod_string)
    outfile.close()
    return None
