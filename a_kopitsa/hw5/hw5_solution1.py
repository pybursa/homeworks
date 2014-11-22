#!/usr/bin/env python
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
"""

__author__ = "Andrey Kopitsa aka a_kopitsa"
__email__ = "andrey.kopitsa@gmail.com"
__date__ = "2014-11-17"

import datetime


class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname, self.first_name, self.birth_date = \
            surname, first_name, birth_date
        if nickname is not None:
            self.nickname = nickname

    def get_age(self):
        date = datetime.datetime(int(self.birth_date[0:4]),
                                 int(self.birth_date[5:7]),
                                 int(self.birth_date[8:10])).strftime('%Y')

        nowdate = datetime.datetime.now().strftime('%Y')
        date = int(nowdate) - int(date)
        return str(date)

    def get_fullname(self):
        return self.surname + " " + self.first_name

