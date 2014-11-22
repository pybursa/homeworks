# -*- coding: utf8 -*-

u"""
Задание 1: вычитка по полной.

УСЛОВИЕ:
дан файл с данными: homeworks/HOMETASKS/hw6/data.csv
Написать функцию modifier(filename), которая должна:
- вычитать данные;
- создать объекты класса Person на основании полученных данных;
- модифицировать данные:
а) добавить графу полного имени (fullname) после графы с именем (name)
б) добавить графу с возрастом (age) в конец.
На выходе получить файл, расширенный указанным образом.

Примечание:
1) смотрите документацию по модулю csv;
(https://docs.python.org/2/library/csv.html?highlight=csv#module-csv)

Пример:
при запуске скрипта (homeworks/.../hw6/hw6_starter.py)
Тестов в этом задании не предусмотрено.
"""

__author__ = "rm_ponomarenko"
__email__ = "ponomarenko.roman@gmail.com"
__date__ = "2014-11-21"

from Person import Person
import csv
import sys


ID = "id"
SURNAME = "surname"
NAME = "name"
FULLNAME = "fullname"
BIRTHDATE = "birthdate"
NICKNAME = "nickname"
AGE = "age"


def modifier(filename):
    """
    The function performs following:
        - subtracts the data from the file;
        - creates objects of a class Person based on received data;
        - modifies data:
            a) adds the full name of the column (fullname)
            after columns named (name)
            b) adds the column with age (age) in the end
    """
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        try:
            csv_data = [row for row in reader]
        except csv.Error as e:
            sys.exit('file {0}, line {1}: {2}'
                     .format(filename, reader.line_num, e))

    phonebook = []
    for row in csv_data:
        phonebook.append(Person(row[SURNAME],
                                row[NAME], row[BIRTHDATE],
                                row[NICKNAME].strip() or None))

    with open(filename, 'wb') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([ID, SURNAME, NAME, FULLNAME,
                         BIRTHDATE, NICKNAME, AGE])
        for index, row in enumerate(phonebook):
            writer.writerow([index + 1, row.surname, row.first_name,
                             row.get_fullname(), row.birth_date,
                             getattr(row, NICKNAME, None), row.get_age()])
