# -*- coding: utf8 -*-

u"""
ДЗ#5.
"""

__author__ = "o_chernyak"
__email__ = "olgache73@gmail.com"
__date__ = "2014-11-20"

from datetime import date, datetime

class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname = " "):
        self.first_name, self.surname, self.birth_date = first_name, surname, birth_date
    
    def get_fullname(self):
        u"""Получаем имя, фамилию"""
        print self.surname, self.first_name
        
    def get_age(self):
        u"""Получаем возраст"""
        today = datetime.today()
        birthday = datetime.strptime(self.birth_date, '%Y-%m-%d')
        age = today.year - birthday.year
        if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
            age = age - 1
        print age
  

