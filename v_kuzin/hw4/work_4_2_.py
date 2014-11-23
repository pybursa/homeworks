#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 4. 2
#

u"""
Программа ограничения размера строки
"""

__author__ = "kuzin.valeriy"
__email__ = "kuzin.valeriy@gmail.com"
__date__ = "2014-11-16"

input_text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.\
 Donec rutrum congue leo eget malesuada.'

#print input_text

def cut_text(input_txt, size):

	u"""Обрезание текста до указанной величины"""

	if size in '':
		return input_txt

	else:
		rest = ''

		for i in range(0, int(size)):

			if i < size:
				rest = rest + input_txt[i]

		return rest

def correct_text(data_cut):

	u"""Оформление текста после обрезания, согласно задания"""

	if ' ' not in data_cut:

		data_cut = data_cut[:-3] + "..."
		return data_cut

	elif data_cut[-1:] in '.' or data_cut[-2:] in ". ":

		return data_cut

	else:
		for n, m in enumerate(data_cut[::-1]):

			if n == 0 and m in " " :

				data_cut = data_cut[:-3] + "..."
				return data_cut
				break

			if m in " " and n!=0:

				data_cut = data_cut[:-(n+1)] + "..."
				return data_cut
				break

def input_control():

	u"""Ввод размера ограничения строки"""

	while True:

		size_rest = raw_input('Please input size your text: ')

		if size_rest.isdigit() or size_rest in '':

			return size_rest
			break

		else:
			print "Please enter the number!"


enter_size = input_control()
first_cut = cut_text(input_text, enter_size)
output = correct_text(first_cut)

print output
