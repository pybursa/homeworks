#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
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
__author__ = 'andrey matukhno'

import datetime


class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname="NA"):
        self.surname = surname
        self.first_name = first_name
        if nickname != "NA":
            self.nickname = nickname
        self.birth_date = datetime.date(int(birth_date[:4]), int(birth_date[5:7]), int(birth_date[8:]))

    def get_age(self):
        age = datetime.date.today().year - self.birth_date.year
        return str(age)

    def get_fullname(self):
        fullname = self.surname + ' ' + self.first_name
        return fullname