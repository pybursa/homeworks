# coding=utf-8
"""
Implementation of method modifing csv file using Person class
"""
import csv
from hw5_solution1 import Person


def modifier(filename):
    '''
    Modifies original csv file with person data
    :param filename: str
    '''
    with open(filename, "r") as data_file:
        data = csv.reader(data_file)
        header = data.next()
        persons = [Person(*row[1:]) for row in data]
    header.insert(header.index('name') + 1, 'fullname')
    header.append('age')

    with open(filename, 'w') as data_file:
        data = csv.writer(data_file)
        data.writerow(header)
        for id, person in enumerate(persons, start=1):
            data.writerow([id, person.surname, person.first_name,
                           person.get_fullname(), person.birth_date,
                           getattr(person, 'nickname', ''), person.get_age()])
