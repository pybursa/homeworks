# -*- coding: utf-8 -*- 
# Assignment #6.1 - 
#
# Procedure modifier retrieves data from the input file
# and creates object Person based on the file content
# Once the object is created, the data are modified as follows:
# - Adds column "fullname" after the column "name" 
# - Adds column "age" as the last column

import csv
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

def modifier(filename):
    f_i = open(filename,"r")
    #-----------------------------------------------
    # Part I - storing columns in Object attributes	
    #-----------------------------------------------
    reader = csv.reader(f_i, dialect=csv.excel, delimiter=",")

    array_in = [[col for col in row] for row in reader]
    # I still don't get why the last range index should be 6
    person_list=[Person(array_in[i][1],array_in[i][2],array_in[i][3],array_in[i][4]) for i in range(1,5)]   
    #-----------------------------------------------
    # Part II - modifying the csv file	
    #-----------------------------------------------
    # Truncate the existing file
    f_i.close()
    f_o = open("data.csv","w")
    f_o.seek(0)
    f_o.truncate()
    writer = csv.writer(f_o, dialect=csv.excel, delimiter=",")
    # Form and write the header
    array_out=[]
    array_in[0].insert(3,"full name")
    array_in[0].append("age") 
    writer.writerow(array_in[0])
    # Form each data line and write it to the header
    for i, item in enumerate(person_list):
        writer.writerow([i, item.surname, item.first_name,item.get_fullname(),item.birth_date,item.nickname,item.get_age()])
    return

modifier("data.csv")