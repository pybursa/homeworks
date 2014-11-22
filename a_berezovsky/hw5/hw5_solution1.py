# coding=utf-8
"""
Implementation of simple Person class
"""

__author__ = "Oleksandr Berezovskyi"
__email__ = "ror191505@gmail.com"
__date__ = "2014-11-18"

from datetime import datetime


class Person(object):
    """
    Class represents information about user
    """

    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = self._process_birth_date(birth_date)
        if nickname:
            self.nickname = nickname

    @staticmethod
    def _process_birth_date(birth_date):
        return datetime.strptime(birth_date, "%Y-%m-%d").date()

    def get_age(self):
        """
        Returns number of full years from birth till nowadays
        :return:str
        """
        days_delta = datetime.now().date() - self.birth_date
        years_delta = days_delta.days / 365
        return str(years_delta)

    def get_fullname(self):
        """
        Returns full surname and fist name in single string
        :return: str
        """
        return "%s %s" % (self.surname, self.first_name)
