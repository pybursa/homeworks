# coding=utf-8
import csv
from person import Person


def modifier(filename):
    '''
    Insert required data
    '''
    with open(filename, "r") as csv_file:
        data = csv.reader(csv_file)
        head = data.next()
        persons = []
        for row in data:
            persons.append(Person(*row[1:]))
        head.insert(head.index('name') + 1, 'fullname')
        head.append('age')

    with open(filename, 'w') as csv_file:
        data = csv.writer(csv_file)
        data.writerow(head)
        for id, person in enumerate(persons, start=1):
            data.writerow([id, person.surname, person.first_name,
                           person.get_fullname(), person.birth_date,
                           getattr(person, 'nickname', ''), person.get_age()])
