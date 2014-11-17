#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 4. 1
#

u"""
Программа определения процентного отношения букв в тексте
"""

__author__ = "kuzin.valeriy"
__email__ = "kuzin.valeriy@gmail.com"
__date__ = "2014-11-16"


input_text = "q Tyoioiooin_U#!{}."
print input_text
input_text = input_text.lower()


def choice_letter(input_text):

	u"""Выбор используемых букв для подсчета"""

	alphabet = ''

	for i in input_text:

		if i not in alphabet and i.isalpha():
			alphabet = alphabet + i

	return alphabet

def seek_letter(letter):

	u"""Вычисление процентного отношения буквы в тексте"""

	count_letter = 0
	count_all_letters = 0

	for i in input_text:

		if i.isalpha():

			count_all_letters += 1

		if i is letter:

			count_letter += 1

	percent = round((float(count_letter)/float(count_all_letters)*100),1)

	lib_persent = dict({letter : percent})

	return lib_persent

def build_lib(input_text):

	u"""Запись результата в библиотеку"""

	alphabet = choice_letter(input_text)
	result = {}

	for i in alphabet:

		add = seek_letter(i)
		result.update(add)

	return result

result_lib = build_lib(input_text)

print result_lib
