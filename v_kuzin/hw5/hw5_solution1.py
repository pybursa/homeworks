#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Оеализовать класс Person, который отображает запись в книге контактов.

Класс имеет 4 атрибута:
- surname - строка - фамилия контакта (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный)

Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
атрибутами.

Также класс имеет 2 метода:
- get_age() - считает возраст контакта в полных годах на дату вызова и
возвращает строку вида: "27";
- get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
контакта;

"""

__author__ = "kuzin.valeriy"
__email__ = "kuzin.valeriy@gmail.com"
__date__ = "2014-11-19"

import datetime
from datetime import datetime, date

class Person(object):
	def __init__ (self, surname, first_name, birth_date, nickname=''):
		self.first_name = first_name
		self.surname = surname
		self.birth_date = birth_date
		if nickname != '':
			self.nickname = nickname
		self.name_all = None
		self.today_date = None
		self.delta = None
		self.adg_old = None



	def get_fullname(self):
		u"""формирование строки с полным именем"""
		self.name_all = self.surname + ' ' + self.first_name
		return self.name_all


	def get_age(self):
		u"""расчет возраста"""

		self.today_date = datetime.today()
		self.birth_date = datetime.strptime(self.birth_date, '%Y-%m-%d')

		self.delta = self.today_date - self.birth_date
		self.adg_old = self.delta.days / 365

		return self.adg_old
