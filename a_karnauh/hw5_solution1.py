# -*- coding: utf8 -*-

u"""
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

__author__ = "anna-karnaukh"
__email__ = "anna.karnaukh1@gmail.com"
__date__ = "2014-11-19"


import time
from datetime import datetime
from datetime import date


class Person(object):
    u"""Класс отображает запись в книге контактов."""
    def __init__(self, surname, first_name, birth_date, nickname=None):
        u"""Конструктор класса"""
        self.surname = surname
        self.first_name = first_name
        if nickname is not None:
            self.nickname = nickname
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()


    def get_age(self):
        u"""Возвращает строку с ворастом контакта
        в полных годах на дату вызова.
        """
        return str((date.today()- self.birth_date).days/365)
       

    def get_fullname(self):
        u"""Возвращает строку с полным именем человека"""
        return '%s %s' % (self.surname, self.first_name)

