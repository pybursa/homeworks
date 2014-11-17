# -*- coding: utf-8 -*-

u"""
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), 
в котором эта буква встречается в тексте.
Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.
"""

__author__ = "anna-karnaukh"
__email__ = "anna.karnaukh1@gmail.com"
__date__ = "2014-11-16"


def frequency_of_letters(text):
	u"""
	Подсчитывает частоту вхождения буквы в заданую строку.
	Принимает строку text, выводит словарь result (ключ - буква, значение - процент (до десятых), 
	в котором эта буква встречается в тексте.).
	"""
	text = text.lower()
	value = 0
	subresult = {}
	result = {}
	length = 0
	for char in text:
		if char.isalnum() == True:
			if char not in subresult.keys():
				value = text.count(char)
				subresult[char] = value
			length += 1
	for k, v in subresult.iteritems():
		result[k] = round(float(v)/length*100, 1)
	return result
