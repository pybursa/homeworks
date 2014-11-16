# -*- coding: utf8 -*-

u"""
ДЗ №4
Решение задачи №1 - Частота букв
Условие:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква 
встречается в тексте.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}

"""
def solution1(st):
	"""
	This function creates a dictionary where keys are the characters and the values
	show the percentage of how many times this character occurs in the string.
	What to do:
	1. lower the string
	2. dictionary (char - how many times)
	3. change the value to calculate percentage
	""" 
	dic = {}
	for i in st.lower():
	    if dic.has_key(i):
		     dic[i] += 1
	    elif i.isalpha():
		    dic[i] = 1
	
	for i in dic.keys():
	    dic[i] = dic[i] * 100.0 / len(st)

	return dic


