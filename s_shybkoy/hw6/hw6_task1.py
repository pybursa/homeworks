#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Задание 6.1: вычитка по полной.

УСЛОВИЕ:
дан файл с данными: homeworks/HOMETASKS/hw6/data.csv
Написать функцию modifier(filename), которая принимает имя файла и должна:
- вычитать данные из переданного файла;
- создать объекты класса Person на основании полученных данных;
- модифицировать данные в файле:
а) добавить графу полного имени (fullname) после графы с именем (name)
б) добавить графу с возрастом (age) в конец.
На выходе получить файл, расширенный указанным образом.
"""


__author__ = "Sergei Shybkoi"
__copyright__ = "Copyright 2014, The Homework Project"
__email__ = "heap_@mail.ru"
__status__ = "Production"
__date__ = "2014-11-22"


import os
import datetime
import csv


class Person(object):
    u"""Класс Person"""
    def __init__(self, surname, first_name, birth_date, nickname=None):
        u"""Инишн класса"""
        try:
            var_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
            res_date = datetime.date(var_date.year,
                                     var_date.month, var_date.day)
        except TypeError:
            raise TypeError("You must provide birth date in correct format "
                            "(YYYY-MM-DD)!")
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")
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
            return str(delta)
        else:
            return "0"

    def get_fullname(self):
        u"""Метод выводит и возвращаем полное имя экземпляра класса Person"""
        return self.surname + " " + self.first_name


class CsvHandler(object):
    u"""Класс видоизменяет входящий csv-файл"""
    def __init__(self, file_name):
        u"""Инишн класса"""
        if os.path.isfile(file_name):
            self.file_name = file_name
        else:
            raise IOError("File not found!")

    def modify_file(self):
        u"""Метод изменения csv-файла"""
        input_file = open(self.file_name, "rU")
        read_csv = csv.DictReader(input_file, fieldnames=['id', 'surname',
                                  'name', 'birthdate', 'nickname'])
        res_dic = []
        for row in read_csv:
            if row.values() == row.keys():
                continue
            per = Person(row['surname'], row['name'], row['birthdate'])
            row['fullname'] = per.get_fullname()
            row['age'] = per.get_age()
            res_dic.append(row)
        input_file.close()
        output_file = open(self.file_name, "wb")
        write_csv = csv.DictWriter(output_file, fieldnames=['id', 'surname',
                                   'name', 'fullname', 'birthdate',
                                   'nickname', 'age'])
        write_csv.writeheader()
        write_csv.writerows(res_dic)
        output_file.close()


def modifier(filename):
    u"""Функция обработки csv-файла"""
    try:
        x = CsvHandler(filename)
        x.modify_file()
        return "Modified successfully!"
    except IOError:
        return "File " + filename + "not found!"
    except TypeError:
        return "Incorrect input data format!"
    except ValueError:
        return "Incorrect input data format!"
