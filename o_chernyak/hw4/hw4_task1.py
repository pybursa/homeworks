# -*- coding: utf8 -*-
u"""
ДЗ#4. Задача 1
"""
__author__ = "OlgaChernyak"
__email__ = "olgache73@gmail.com"
__date__ = "2014-11-16"


text_in = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada."
unique_letters = set(text_in.lower()) #Нахождение уникальных символов в тексте
dic_out = {}

u"""Подсчет символов в тексте"""
def count_symbols(text):
    symbols_qu = 0
    for n in text:
        symbols_qu +=1
    return symbols_qu

u"""Вычисление процентного соотношение букв в тексте."""
def hw4_percentage(text):
    symbols_in_text = count_symbols(text_in)
    for i in unique_letters:
        letters_quantity = sum(j == i for j in text.lower())
        persent_in_text = (float(letters_quantity)/symbols_in_text)*100
        dic_out.update({i: round(persent_in_text)})
    print dic_out

hw4_percentage(text_in)

        
