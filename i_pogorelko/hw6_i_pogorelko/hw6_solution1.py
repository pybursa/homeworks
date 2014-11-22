#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "pro"
__email__ = "i.pogorelko@gmail.com"
__date__ = "2014-11-22"

import csv
import datetime
from datetime import date

def modifier(filename):

    
    class Person(object):
        def __init__(self, ident, surname, name, bdata, nickname=None):
            self.ident = ident
            self.surname = surname
            self.name = name
            dt = bdata.split("-")
            #print 'bdata', bdata
            #print 'dt', dt
            birth_date = datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))
            self.birth_date = birth_date
            if nickname is not None:
                self.nickname = nickname
            else:
                self.nickname = ''

        def get_fullname(self):
            fullname = self.surname + " " + self.name
            return fullname

        def get_age(self):
            now = datetime.date.today()
            birthday = self.birth_date
            age  = now.year - birthday.year
            return str(age)
            

    b = []
    fp = open(filename,"rb")

    with fp as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        n = 0
        for row in reader:
            if n > 0:
                if row[4] != '':
                    user = Person(row[0], row[1], row[2], row[3], row[4])
                else:
                    user = Person(row[0], row[1], row[2], row[3])
                #print 'user:',  user.nickname
                b.append(user)
            n += 1
        #print 'b = ', b
    fp.close()
    fp = open(filename,"wb")

    with fp as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['id','surname','name','fullname','birthdate','nickname','age'])
        for row in b:
            #print row
            writer.writerow([row.ident, row.surname, row.name, row.get_fullname(), row.birth_date, row.nickname, row.get_age()])
            #print b
    fp.close()

