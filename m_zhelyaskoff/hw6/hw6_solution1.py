# -*- coding: utf-8 -*-

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
"""

__author__ = "Mihail Zhelyaskov aka m_zhelyaskoff"
__version__ = "0.0.1"
__maintainer__ = "Mihail Zhelyaskov"
__email__ = "mzhelyaskov@yandex.ru"
__status__ = "Production"

import csv
import os.path

from Person import Person


def modifier(filename):
    """Modifies a file CSV. Adds a new column in the data structure"""
    try:
        assert os.path.exists(filename)
    except:
        raise ValueError('file "'+str(filename)+'" does not exist!')
    try:
        persons = {}
        csv_file = open(filename, 'rU')
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            person_id = int(line['id'])
            surname = line['surname']
            name = line['name']
            birth_date = line['birthdate']
            nickname = line['nickname']
            person = Person(surname, name, birth_date, nickname)
            persons[person_id] = person
        csv_file.close()

        csv_file = open(filename, 'w')
        fieldnames = ['id',
                      'surname',
                      'name',
                      'fullname',
                      'birthdate',
                      'nickname',
                      'age']
        csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(fieldnames)
        for person_id in persons.keys():
            person = persons[person_id]
            record = [person_id,
                      person.surname,
                      person.first_name,
                      person.get_fullname(),
                      person.birth_date,
                      person.nickname,
                      person.get_age()]
            csv_writer.writerow(record)
    finally:
        csv_file.close()