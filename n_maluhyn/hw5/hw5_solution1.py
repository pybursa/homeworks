#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from datetime import date

__author__ = "malukhin"


class Person:

    surname = ''
    first_name = ''
    birth_date = date.today()

    def __init__(self, surname, first_name, birth_date, nickname=''):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.date(int(birth_date[0:4]), int(birth_date[5:7]), int(birth_date[8:10]))

        if nickname != '':
            self.nickname = nickname

    def get_age(self):
        r = date.today() - self.birth_date
        print dir(r)
        return str(int(r.days / 365.25))

    def get_fullname(self):
        return self.surname + ' ' + self.first_name
