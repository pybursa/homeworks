__author__ = "Elena Sharovar"
__date__ = '2014-11-19'

import datetime

class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname = None):
        self.surname = surname
        self.first_name = first_name

        elements = birth_date.split("-")
        year = int(elements[0])
        month = int(elements[1])
        day = int(elements[2])
        self.birth_date = datetime.date(year, month, day)

        if nickname is not None:
            self.nickname = nickname

    def get_fullname(self):
        return self.surname + ' ' + self.first_name

    def get_age(self):
        now = datetime.datetime.now()
        return str(now.year - self.birth_date.year)


