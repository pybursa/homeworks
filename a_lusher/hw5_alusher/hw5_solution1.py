# -*- coding: utf-8 -*- 

# Assignment #5.1 - Class Person accepts last and first names, 
#	optional nickname, and datebirth
#	The class also contains two functions - get_age() that returns persons 
#	and get_fullname() that returns full name
#		
# Example: Person.get_age() and Person.get_fullname()

__author__ = "a_lusher"
__date__ = "2014-11-18"

import datetime

class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = str(surname)
	self.first_name = str(first_name)
	self.birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
	if nickname!=None:
		self.nickname=str(nickname)

    def get_fullname(self):
        return self.surname+" "+self.first_name

    def get_age(self):
        now = datetime.datetime.now()
        year_diff=now.year-self.birth_date.year
        month_diff=now.month-self.birth_date.month
        day_diff=now.day-self.birth_date.day
        if year_diff<0:
            return "This can't be true"
        else:
            if month_diff>=0 and day_diff>=0:
                return str(year_diff)
            else:
                return str(year_diff-1)