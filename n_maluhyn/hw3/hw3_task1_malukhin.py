#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание 1: И снова гласные.
#
# УСЛОВИЕ:
# Посчитать количество гласных в каждом слове текста.
# Вывести максимальное количество гласных в одном слове.
#
# Текст:
# Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
#
# Гласные: A, E, I, O, U, Y

def number_of_vowels(test_str):
    sentence = test_str.split(' ')
    largest = 0
    largest_num = 0
    for (number, word) in enumerate(sentence):
        vowels = 0
        for letter in word:
            if letter.isalpha():
                if letter.lower() in 'aeiouy':
                    vowels += 1
        if largest < vowels:
            largest = vowels
            largest_num = number
    print str(largest) + ' in ' + sentence[largest_num]
    

test_str =  'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'
print number_of_vowels(test_str)
