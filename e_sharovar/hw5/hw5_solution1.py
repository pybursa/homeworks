"""
Homework 5, task 1
Person class
"""

__author__ = "Elena Sharovar"
__date__ = '2014-11-19'

import datetime

class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname = None):
        self.surname = surname
        self.first_name = first_name

        elements = birth_date.split("-")
        elements = map(int, elements)
        self.birth_date = datetime.date(elements[0], elements[1], elements[2])

        if nickname is not None:
            self.nickname = nickname

    def get_fullname(self):
        return self.surname + ' ' + self.first_name

    def get_age(self):
        now = datetime.datetime.now()
        return str(now.year - self.birth_date.year)


