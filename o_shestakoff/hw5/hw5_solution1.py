from datetime import datetime


class Person(object):
    def __init__(self, surName, firstName, birth_date, nickname=None):
        self.surname = surName
        self.first_name = firstName
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        self.nickname = nickname

    def get_age(self):
        return str(int(((datetime.now() - datetime(self.birth_date.year, self.birth_date.month, self.birth_date.day)).days / 365.0)))

    def get_fullname(self):
        return self.surname + ' ' + self.first_name



# p = Person('Shestakov', 'Oleg', '1991-06-17', 'gremlin_lee')
# print p.get_age()
# print p.get_fullname()