# -*- coding: utf-8 -*-

__author__ = "Mihail Zhelyaskov aka m_zhelyaskoff"
__copyright__ = "Copyright 2014, The Homework Project"
__version__ = "0.0.1"
__maintainer__ = "Mihail Zhelyaskov"
__email__ = "mzhelyaskov@yandex.ru"
__status__ = "Production"

import datetime


class Person(object):
    """Describes the contact in the phone book.

    Keyword arguments:
    surname -- surname of the person (required)
    first_name -- first_name of the person (required)
    birth_date -- birth_date of the person (required)
    nickname -- nickname of the person (default None)
    """

    def __init__(self, surname, first_name, birth_date, nickname=None):
        """Constructor for Person"""
        self.surname = surname
        self.first_name = first_name
        if nickname is not None:
            self.nickname = nickname
        try:
            date_object = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
            self.birth_date = date_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_age(self):
        """Return the number of years for this moment"""
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month:
            age -= 1
        elif today.month == self.birth_date.month:
            if today.day < self.birth_date.day:
                age -= 1
        return str(age)

    def get_fullname(self):
        """Return the fullname"""
        fullname = self.surname + " " + self.first_name
        return fullname