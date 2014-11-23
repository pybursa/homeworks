# -*- coding: utf-8 -*-
"""
Class 'Person' and its methods
"""

__author__ = "marie_s"
__email__ = "smirnitskayamp@gmail.com"
__date__ = "2014-11-20"

from datetime import datetime, date, time


class Person(object):


    def __init__(self, surname, first_name, birth_date, nickname=None):
        """
        User info
        """
        self.surname = surname
        self.first_name = first_name
        if nickname:
            self.nickname = nickname
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()


    def get_age(self):
        """
        The method calculates the age of the person
        """
        age = datetime.now().date() - self.birth_date
        return str(age.days / 365)


    def get_fullname(self):
        """
        This method returns the full name of the person
        """
        return self.surname + " " + self.first_name
