# -*- coding: utf8 -*-

u"""
Решение задачи#1 ДЗ#5 - классный Человек.

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


Примечание:
1) смотрите документацию по модулю datetime;

2) при создании атрибута birth_date из строки типа "2014-12-31" необходимо:
 - определить какая информация нужна для создания объекта datetime.date,
 - получить эти данные из строки - разобрать ее (достать из нее  отдельно,
 год, месяц, число),
 - на основании этой информации создать специальный объект datetime.date,
 - поместить этот спец.объект в атрибут экземпляра класса;


Пример:

при запуске скрипта (homeworks/.../hw5/hw5_starter.py) должны проходить тесты
из файла тестов (homeworks/.../hw5/hw5_tests.py), кот. прилагается.

==============================================================================
"""


__author__ = "a_kushnaryoff"
__date__ = "2014-11-14"


from datetime import datetime


class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self._birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")
        self.birth_date = self._birth_datetime.date()

        self._fullname = None
        self._age_delta = None
        self._age_year = None

        if type(nickname) is str:
            self.nickname = nickname

    def get_fullname(self):
        self._fullname = self.surname + " " + self.first_name
        return self._fullname

    def get_age(self):
        self._age_delta = datetime.now().date() - self.birth_date
        self._age_year = str(int(self._age_delta.days/365.25))
        return self._age_year

