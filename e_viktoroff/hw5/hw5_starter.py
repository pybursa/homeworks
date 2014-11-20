# -*- coding: utf8 -*-


__autor__ = "Viktorov Eugene"
__email__ = "jekafromua@gmail.com"
__date__ = "2014-11-19"


class Preson(object):

    u"""создает объекты фомой записной книжи

    .get_age - возвращает возраст объекта
    .get_fullname - возвращает имя объекта"""


    def __init__(self, surname, first_name, birth_date, nickname=""):

        from datetime import datetime

        self.surname, self.first_name = surname, first_name
        self.nickname = nickname
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):

        from datetime import datetime

        today_date = datetime.today()
        age = [0, 0, 0]
        age[0] = today_date.year - self.birth_date.year
        age[1] = today_date.month - self.birth_date.month
        age[2] = today_date.day - self.birth_date.day
        if age[0] < 0:
            return 'incorrect date of birth'
        for i in age:
            if i < 0:
                return age[0] - 1
        return age[0]

    def get_fullname(self):
        full_name = self.surname + " " + self.first_name
        if self.nickname != '':
            full_name = full_name + ', nickname: ' + self.nickname
        return full_name



def inlet():
    a = raw_input("surname - ")
    b = raw_input('first name - ')
    c = raw_input('nickname - ')
    d = raw_input('enter DOB in format: year-month-day. e.g. - 1991-10-01')
    return Preson(a, b, d, c)

out = inlet()
print out.get_age()
print out.get_fullname()

