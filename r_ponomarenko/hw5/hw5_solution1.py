# -*- coding: utf8 -*-

u"""
Задание 1: классный Человек.

УСЛОВИЕ: Реализовать класс Person, который отображает запись в книге контактов.

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

Примечание:
1) смотрите документацию по модулю datetime;
2) при создании атрибута birth_date из строки типа "2014-12-31" необходимо:
- определить какая информация нужна для создания объекта datetime.date,
- получить эти данные из строки - разобрать ее (достать из нее отдельно,
год, месяц, число),
- на основании этой информации создать специальный объект datetime.date,
- поместить этот спец.объект в атрибут экземпляра класса;
"""

__author__ = "rm_ponomarenko"
__email__ = "ponomarenko.roman@gmail.com"
__date__ = "2014-11-18"

from datetime import datetime
from datetime import date


class Person():
    """This class implements an entry in a phonebook for a person.

    Attributes:
      surname (str): Surname of a person in the phonebook.
      first_name (str): First name of a person in the phonebook.
      birth_date (date): Date of birth of a person in the phonebook.
      [optional] nickname (str): Nickname of a person in the phonebook.
    """
    def __init__(self, surname, first_name, birth_date, nickname=""):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        if nickname:
            self.nickname = nickname

    def get_age(self):
        """
        Returns the age of a person (completed years) as string value.
        """
        return str((date.today() - self.birth_date).days / 365)

    def get_fullname(self):
        """
        Returns a string that reflects the full name of a person
        (surname + first name).
        """
        return "%s %s" % (self.surname, self.first_name)
