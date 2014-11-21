# coding=utf-8
"""
Modification of a csv file
"""

import csv
from hw5_solution1 import Person


def modifier(file):
    """
     This function accepts a csv file and modifies it according to the task:
    creates Person classes, adds fullname and age columns
    """
    fp = open(file, "r")
    csv_reader = csv.reader(fp)
    new = []
    for i in csv_reader:
        if i[0] == "id":
            index = i.index('name') + 1
            i.insert(index, "fullname")
            i.append("age")
        else:
            person = Person(*i[1:])
            i.insert(index, person.get_fullname())
            i.append(person.get_age())
        new.append(i)

    fw = open(file, "w")
    csv_writer = csv.writer(fw)
    for i in new:
       csv_writer.writerow(i)


