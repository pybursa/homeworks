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

Пример:
при запуске скрипта (homeworks/.../hw5/hw5_starter.py) должны проходить тесты
из файла тестов (homeworks/.../hw5/hw5_tests.py), кот. прилагается.
"""

__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-18"
__license__ = "GPL"
__version__ = "0.0.1"

import datetime


class Person(object):
    u"""Класс "Классный человек" """

    def __init__(self, surname, name, birthdate, nickname=False):
        u"""Инициализация атрибутов"""
        self.surname = surname
        self.first_name = name
        self.nickname = nickname
        birthday_list = birthdate.split('-')
        for i in range(len(birthday_list)):
            birthday_list[i] = int(birthday_list[i])
        self.birth_date = datetime.date(
            birthday_list[0],
            birthday_list[1],
            birthday_list[2])

    def get_age(self):
        u"""Метод выдающий возраст классного человека"""
        now_date = datetime.date.today()
        result = now_date.year - self.birth_date.year
        birthday = datetime.date(
            now_date.year,
            self.birth_date.month,
            self.birth_date.day)
        if birthday > now_date:
            result -= 1
        return str(result)

    def get_fullname(self):
        u"""Метод выдающий полное имя классного человека"""
        result = self.surname + ' ' + self.first_name
        return result
