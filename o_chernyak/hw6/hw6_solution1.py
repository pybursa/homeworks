# -*- coding: utf-8 -*-

u"""
ДЗ 6.
Написать функцию modifier(filename), которая принимает имя файла и должна:
- вычитать данные из переданного файла;
- создать объекты класса Person на основании полученных данных;
- модифицировать данные в файле:
а) добавить графу полного имени (fullname) после графы с именем (name)
б) добавить графу с возрастом (age) в конец.
"""

__author__ = "o_chernyak"
__email__ = "olgache73@gmail.com"
__date__ = "2014-11-23"


import csv
from hw5_solution1 import Person


def csv_to_class():
    with open('data.csv','r') as csv_in:
        extract = csv.DictReader(csv_in, dialect='excel')
        persons = []
        for row in extract:
            persons.append(row)
        return persons

def modifier(filename):
    """
    for i in range(len(csv_to_class())):
        person = Person()
        person += persons[i]
    """
    with open(filename,'r') as csv_in:
        with open('output.csv', 'w') as csv_out:
            writer = csv.writer(csv_out)
            for row in csv.reader(csv_in):
                if row[0] == "id":
                    writer.writerow(row+["Age"])
                else:
                    writer.writerow(row+[""])
     
    csv_in.close()
    csv_out.close()

