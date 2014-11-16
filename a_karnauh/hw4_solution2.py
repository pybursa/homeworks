# -*- coding: utf-8 -*-

u"""
УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.
"""

__author__ = "anna-karnaukh"
__email__ = "anna.karnaukh1@gmail.com"
__date__ = "2014-11-16"

def afterword(text, limit = ""):
	u"""Получает строку text и ограничение длины строки limit. Выводит обрезанную строку."""
	if limit < 4:
		return "Invalid limit"
	if len(text) <= limit:
		return text
	split_text = text.split()
	if len(split_text[0]) >= limit - 3:
		return text[0:limit - 3] + "..."
	result_text = "" 
	for element in split_text:
		if len(result_text + element) <= limit - 3:
			result_text += element + " "
		else:
			return result_text.strip() + "..."
