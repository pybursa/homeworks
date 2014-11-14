#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание 2: Самое длинное слово.
#
# УСЛОВИЕ:
# Найти слово максимальной длины в тексте.
# Вывести это слово. Если таких слов несколько - вывести все.
#
# Текст:
# Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.


def largest_words(seq):
    sentence = seq.split(' ')
    largest = 0
    largest_num = 0
    for (number, word) in enumerate(sentence):
        vowels = 0
        for letter in word:
            if letter.isalpha():
                vowels += 1
        if largest < vowels:
            largest = vowels
    print str(largest)

    for (number, word) in enumerate(sentence):
        if len(word) == largest:
            print word

t =  'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'
print largest_words(t)
