#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv


class Person(object):
    def __init__(self, id, surname, name, birthday, nickname, fullname=None,
                 age=None):
        self.id = id
        self.surname = surname
        self.name = name
        self.birthday = birthday
        self.nickname = nickname
        if fullname is not None:
            self.fullname = fullname
        elif age is not None:
            self.age = age


def modifier():
    fp = open("data.csv", "r+")
    line = fp.readlines()
    fp.seek(line[0].find("birthdate"))
    fp.write("fullname," + line[0][line[0].find("birthdate"):-1:] + ",age\n")
    count = 1
    while count <= 5:
        listline1 = line[count].split(",")
        listline1.append("")
        listline1.append("")
        listline1[5] = listline1[4][:-1]
        listline1[4] = listline1[3]
        listline1[3] = ""
        listline1 = ",".join(listline1) + ",\n"
        fp.write(listline1)
        count += 1
    fp.seek(0)
    reader = csv.reader(fp)
    next(reader)
    for row in reader:
        row[2] = Person(row[0], row[1], row[2], row[3], row[4])
    fp.close

modifier()

