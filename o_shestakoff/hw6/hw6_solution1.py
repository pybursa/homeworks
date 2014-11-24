#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "o.shestakov"
__email__ = "gremlin.leen@gmail.com"
__date__ = "2014-11-23"

import csv
import os
from datetime import datetime


class Person(object):
    def __init__(self, surName, firstName, birth_date, nickname=None):
        self.surname = surName
        self.first_name = firstName
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        if nickname is not None:
            self.nickname = nickname

    def get_age(self):
        return str(int((
            (datetime.now() - datetime(self.birth_date.year,
                                       self.birth_date.month,
                                       self.birth_date.day)).days / 365.0)))

    def get_fullname(self):
        return self.surname + ' ' + self.first_name


def modifier(file):
    with open(file, 'r+') as f:
        reader = csv.DictReader(f,
                                ['id', 'surname',
                                 'name', 'birthdate',
                                 'nickname'])
        reader.next()
        list_of_heroes = []
        for row in reader:
            p = Person(
                row['surname'],
                row['name'],
                row['birthdate'],
                row['nickname']
            )
            list_of_heroes.append(p)

        os.remove(os.path.abspath(file))

        f = open(file, 'w')

        writer = csv.DictWriter(f, ['id', 'surname', 'name', 'fullname',
                                    'birthdate', 'nickname', 'age'])
        index = 1
        writer.writeheader()
        for i in list_of_heroes:
            modifiedHero = dict()
            modifiedHero['id'] = index
            modifiedHero['surname'] = i.surname
            modifiedHero['name'] = i.first_name
            modifiedHero['fullname'] = i.get_fullname()
            modifiedHero['birthdate'] = i.birth_date
            modifiedHero['nickname'] = i.nickname
            modifiedHero['age'] = i.get_age()
            writer.writerow(modifiedHero)
            index += 1

        f.close()
