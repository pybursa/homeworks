# -*- coding: utf8 -*-

u"""
ДЗ 5
"""

__author__ = "o_chernyak"
__email__ = "olgache73@gmail.com"
__date__ = "2014-11-23"


class Person(object):
    """Represents notebook entry"""
    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        if nickname is not None:
            self.nickname = nickname

