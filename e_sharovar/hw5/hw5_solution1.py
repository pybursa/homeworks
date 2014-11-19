"""
Homework 5, task 1
Person class
"""

__author__ = "Elena Sharovar"
__date__ = '2014-11-19'

import datetime

class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname = None):
        date_elements = birth_date.split("-")
        date_elements = map(int, date_elements)

        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.date(date_elements[0], date_elements[1], date_elements[2])
        if nickname is not None:
            self.nickname = nickname

    def get_fullname(self):
        return self.surname + ' ' + self.first_name

    def get_age(self):
        now = datetime.datetime.now()
        age = now.year - self.birth_date.year
        # month did not came yet
        if (now.month < self.birth_date.month):
            age -= 1
        # day did not came yet
        if now.month == self.birth_date.month:
            if now.day < self.birth_date.day:
                age -= 1
        return str(age)


