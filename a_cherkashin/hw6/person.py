# coding=utf-8
"""
Person class implementation
"""

__author__ = "Alexey Cherkashin"
__email__ = "goodiceweb@gmail.com"

from datetime import datetime


class Person(object):
    """
    Simple Person class
    """

    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = self._process_birth_date(birth_date)
        if nickname:
            self.nickname = nickname


    def _process_birth_date(self, birth_date):
        return datetime.strptime(birth_date, "%Y-%m-%d").date()


    def get_age(self):
        """
        Returns string representation of full year's age
        """
        return str((datetime.now().date() - self.birth_date).days / 365)


    def get_fullname(self):
        """
        Returns fullname
        """
        return "%s %s" % (self.surname, self.first_name)
    
    
    def __str__(self):
        person_card = """
        === Visit Card ===
        Fullname: %s
        Age: %s
        """ % (self.get_fullname(), self.get_age())
        if self.nickname:
            person_card += "Nick: " + self.nickname
        return person_card
