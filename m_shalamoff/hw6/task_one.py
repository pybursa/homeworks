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
"""

__author__ = 'm_shalamov'

import csv

from person import Person


def modifier(file_name):
    u"""Основной метод которы реализует чтение, модификацию данных и запись
    в файл формата csv"""
    source_data = csv_reader(file_name)
    person_list = []
    
    for source_index in range(1, len(source_data)):
        person_list.append(Person(source_data[source_index][1],
                                  source_data[source_index][2],
                                  source_data[source_index][3],
                                  source_data[source_index][4]))
    
    result_list = [['id',
                    'surname',
                    'name',
                    'fullname',
                    'birthdate',
                    'nickname',
                    'age']]

    for person_index in range(len(person_list)):
        result_list.append([str(person_index + 1),
                            person_list[person_index].surname,
                            person_list[person_index].first_name,
                            person_list[person_index].get_fullname(),
                            str(person_list[person_index].birth_date),
                            person_list[person_index].nickname,
                            person_list[person_index].get_age()])

    csv_writer(file_name, result_list)


def csv_reader(file_name):
    u"""Метод позволяющий производить чтение из csv файл"""
    line_list = []
    with open(file_name, 'rb') as fr:
        try:
            reader = csv.reader(fr)
            for row in reader:
                line_list.append(row)
        finally:
            fr.close()
    return line_list


def csv_writer(file_name, source):
    u"""Метод позволяющий производить запись в csv файл"""
    with open(file_name, 'wb') as fw:
        try:
            writer = csv.writer(fw)
            writer.writerows(source)
        finally:
            fw.close()
