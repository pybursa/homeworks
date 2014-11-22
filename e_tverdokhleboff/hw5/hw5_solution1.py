
# -*- coding: utf-8 -*-


__author__ = 'tverdokhlebov'
__email__ = 'evgenij0404@gmail.com'
__date__ = '2014-11-19'

import datetime

class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = birth_date

    def get_fullname(self):
        print self.surname+' '+self.first_name

    def get_age(self):
        year, month, day = map(int, date_entry.split('-'))
        birth_date = datetime.date(year, month, day)
        today = date.today()
        y = today.year - birthday.year
        if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
            y -= 1
        return y
