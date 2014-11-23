# -*- coding: utf8 -*-

u"""
Задание 1: классный Человек.

УСЛОВИЕ:
Реализовать класс Person, который отображает запись в книге контактов.

Класс имеет 4 атрибута:
- surname - строка - фамилия контакта (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный), формат: YYYY-MM-DD

Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
атрибутами.

Также класс имеет 2 метода:
- get_age() - считает возраст контакта в полных годах на дату вызова и
возвращает строку вида: "27";
- get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
контакта;


Примечание:
смотрите документацию по модулю datetime
"""

__author__ = "wowkalucky"
__email__ = "wowkalucky@gmail.com"
__date__ = "2014-11-17"


from datetime import datetime, date


class Person(object):
    """Represents notebook entry"""
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format = "%Y-%m-%d"
            datetime_object = datetime.strptime(birthdate, date_format)
            self.birth_date = datetime_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days // 365.25))

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self. first_name)
