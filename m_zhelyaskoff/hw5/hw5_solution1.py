# -*- coding: utf-8 -*-

u"""
Задание 1: классный Человек.

УСЛОВИЕ:
Реализовать класс Person, который отображает запись в книге контактов.
Класс имеет 4 атрибута:
- surname - строка - фамилия контакта (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный)

Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
атрибутами.

Также класс имеет 2 метода:
- get_age() - считает возраст контакта в полных годах на дату вызова и
возвращает строку вида: "27";
- get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
контакта;
"""

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
    surname -- surname of the person
    first_name -- first_name of the person
    birth_date -- birth_date of the person
    nickname -- nickname of the person (default None)

    """

    def __init__(self, surname, first_name, birth_date, nickname=None):
        """Constructor for Person"""
        self.surname = surname
        self.first_name = first_name
        date_param = birth_date.split('-')
        year = int(date_param[0])
        month = int(date_param[1])
        day = int(date_param[2])
        self.birth_date = datetime.date(year, month, day)
        if nickname is not None:
            self.nickname = nickname

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
