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
"""

__author__ = "Sergei Shybkoi"
__copyright__ = "Copyright 2014, The Homework Project"
__email__ = "heap_@mail.ru"
__status__ = "Production"
__date__ = "2014-11-18"

import datetime


class Person(object):
    u"""Класс Person"""
    def __init__(self, surname, first_name, birth_date, nickname=None):
        u"""Инишн класса"""
        try:
            var_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
            res_date = datetime.date(var_date.year,
                                     var_date.month, var_date.day)
        except TypeError:
            print "Incorrect type of birthday date!"
            res_date = None
        except ValueError:
            print "Wrong value of birthday date!"
            res_date = None
        self.surname = surname
        self.first_name = first_name
        self.birth_date = res_date
        if nickname is not None:
            self.nickname = nickname

    def get_age(self):
        u"""Метод класса подсчитывает и выводит количество полных лет"""
        if self.birth_date is not None:
            today_date = datetime.date.today()
            delta = today_date.year - self.birth_date.year
            if today_date.month <= self.birth_date.month \
               and today_date.day < self.birth_date.day:
                delta -= 1
            print "Age:", delta
            return str(delta)
        else:
            print "No correct data about person's birthday."
            return "0"

    def get_fullname(self):
        u"""Метод выводит и возвращаем полное имя экземпляра класса Person"""
        print self.surname, self.first_name
        return self.surname + " " + self.first_name

