"""
Homework 6, task 1
Read persons from file
"""

__author__ = "Elena Sharovar"
__date__ = '2014-11-19'

import csv
from hw5_solution1 import Person

def modifier(filename):

    f = open(filename, 'r+')
    reader = csv.DictReader(f)

    # read
    rows = []
    for row in reader:
        rows.append(row)

    f.seek(0)

    # add age and full name
    for row in rows:
        p = Person(row['surname'], row['name'], row['birthdate'])
        row['age'] = p.get_age()
        row['full_name'] = p.get_fullname()

    # write
    writer = csv.DictWriter(f, ['id','surname','name', 'full_name', 'birthdate','nickname','age'])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

    f.close()