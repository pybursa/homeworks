# -*- coding: utf-8 -*-

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
- получить эти данные из строки - разобрать ее (достать из нее отдельно,
год, месяц, число),
- на основании этой информации создать специальный объект datetime.date,
- поместить этот спец.объект в атрибут экземпляра класса;
"""

__author__ = 'm_shalamov'

import datetime


class Person(object):
    u"""Основной скрипт который реализует класс Person и его методы"""
    def __init__(self, surname, first_name, birth_date, *args):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.datetime.strptime(birth_date,
                                                     '%Y-%m-%d').date()
        if len(args) > 0:
            self.nickname = args[0]

    def get_fullname(self):
        u"""Метод возвращает конкатенированую строку, содержащую значения
        полей surname и first_name класса Person"""
        return str(self.surname) + ' ' + str(self.first_name)

    def get_age(self):
        u"""Метод возвращает разницу между текущей датой и датой содержащейся
        в поде birth_date класса Person"""
        return str(datetime.datetime.today().year - self.birth_date.year)
