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

__author__ = "k.shym"
__email__ = "ks.shym@gmail.com"
__date__ = "2014-11-18"


from datetime import datetime


class Person:
    u"""Класс описывает модель человека"""

    def __init__(self, surname, first_name, birth_date, nickname=None):
        u"""Конструктор класса"""
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        if nickname:
            self.nickname = nickname

    def get_age(self):
        u"""Возвращает строку с возрастом человека"""
        today = self.birth_date.today()
        bd = self.birth_date
        current = int((today.month, today.day) < (bd.month, bd.day))
        return str(today.year - bd.year - current)

    def get_fullname(self):
        u"""Возвращает строку с полным именем человека"""
        return '%s %s' % (self.surname, self.first_name)
