#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "pro"
__email__ = "i.pogorelko@gmail.com"
__date__ = "2014-11-18"

import datetime
from datetime import date


class Person(object):
    def __init__(self, surname, first_name, bdata, nickname=None):
        self.surname = surname
        self.first_name = first_name
        dt = bdata.split("-")
        birth_date = datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))
        self.birth_date = birth_date
        if nickname is not None:
            self.nickname = nickname
        
    def get_fullname(self):
        return " ".join((self.surname, self.first_name))

    def get_age(self):
        now = datetime.date.today()
        birthday = self.birth_date
        age  = now.year - birthday.year
        return str(age)
