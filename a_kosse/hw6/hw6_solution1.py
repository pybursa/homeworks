# -*- coding: utf-8 -*-
u"""
Решение задачи#1 ДЗ#6 - вычитка по полной.

УСЛОВИЕ:
дан файл с данными: homeworks/HOMETASKS/hw6/data.csv

Написать функцию modifier(filename), которая принимает имя файла и должна:
- вычитать данные из переданного файла;
- создать объекты класса Person на основании полученных данных;
- модифицировать данные в файле:
а) добавить графу полного имени (fullname) после графы с именем (name)
б) добавить графу с возрастом (age) в конец.

На выходе получить файл, расширенный указанным образом.

Примечание:
1) смотрите документацию по модулю csv;
(https://docs.python.org/2/library/csv.html?highlight=csv#module-csv)


Запускать через скрипт (homeworks/.../hw6/hw6_starter.py)

Тестов в этом задании не предусмотрено.
"""
__author__ = "Alexander Kosse aka a_kosse"
__email__ = "aleksandr.kosse@gmail.com"
__date__ = "2014-11-23"
__license__ = "GPL"
__version__ = "0.0.1"

import csv
from person import Person


def modifier(file_name):
    u"""Основная функция ДЗ"""
    input_file = open(file_name, 'rb')
    reader = csv.DictReader(input_file)
    field_names = reader.fieldnames
    data_list = []
    for row in reader:
        data_list.append(row)
        var_class = Person(
            data_list[-1]['surname'],
            data_list[-1]['name'],
            data_list[-1]['birthdate'],
            data_list[-1]['nickname'])

        data_list[-1]['fullname'] = var_class.get_fullname()
        data_list[-1]['age'] = var_class.get_age()
    field_names.append('fullname')
    field_names.append('age')
    input_file.close()
    output_file = open(file_name, 'wb')
    writer = csv.DictWriter(output_file, field_names)
    writer.writeheader()
    for str_data in data_list:
        writer.writerow(str_data)
    output_file.close()

