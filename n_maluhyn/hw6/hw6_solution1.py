#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from datetime import date
import csv

__author__ = "malukhin"


class Person:
    # Person initializer
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.date(int(birth_date[0:4]), int(birth_date[5:7]), int(birth_date[8:10]))

        if nickname is not None:
            self.nickname = nickname

    # Return age of person in str.
    def get_age(self):
        r = date.today() - self.birth_date
        print dir(r)
        return str(int(r.days / 365.25))

    # return fullname of person.
    def get_fullname(self):
        return self.surname + ' ' + self.first_name


# Read out file, create dictionary of persons, write in output file entity list with additional parameters.
def modifier(file_path):
    try:
        csv_data = csv.reader(file(file_path))
    except StandardError:
        raise StandardError("Can not read the file " + file_path)

    data = []
    for row in csv_data:
        data.append(row)
    data = data[1:]
    data_persons = []
    for row in data:
        current_person = Person(row[1], row[2], row[3], row[4])
        current_person
        data_persons.append(current_person)

    with open('data-output.csv', 'w') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['id', 'surname', 'name', 'fullname', 'birthdate', 'nickname', 'age'])
        for (i, current_person) in enumerate(data_persons):
            data_writer.writerow([i + 1, current_person.surname, current_person.first_name,
                                 current_person.get_fullname(), current_person.birth_date, current_person.nickname,
                                 current_person.get_age()])
    csv_file.close()
    return None