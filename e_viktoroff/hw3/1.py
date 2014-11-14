# -*- coding: cp1251 -*-
"""Задание 1: И снова гласные.


УСЛОВИЕ:
Посчитать количество гласных в каждом слове текста.
Вывести максимальное количество гласных в одном слове.


Текст:
Proin eget tortor risus.
Cras ultricies ligula sed magna dictum porta.
Proin eget tortor risus.
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.
Donec rutrum congue leo eget malesuada.


Гласные: A, E, I, O, U, Y"""

text = "Proin eget tortor risus.\
 Cras ultricies ligula sed magna dictum porta.\
 Proin eget tortor risus.\
 Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.\
 Donec rutrum congue leo eget malesuada."
print "Proin eget tortor risus.\n\
 Cras ultricies ligula sed magna dictum porta.\n\
 Proin eget tortor risus.\n\
 Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.\n\
 Donec rutrum congue leo eget malesuada.\n"
def vovel(word):
    vovel = 'aeiouy'
    num = 0
    for w in word:
        for v in vovel:
            if w == v:
                num += 1
    return num
def out_words(string):
    string = string.lower().split()

    for i in range(len(string)):
        word = ''
        if '.' in string[i]:
            for l in string[i]:
                if l != ".":
                    word = word + l
            string[i] = word
    return string
def find_vovels(word_vovel):
    longest ={}
    max = 0
    word = ''
    for i in word_vovel.keys():
        if word_vovel[i] > max:
            longest.clear()
            longest = {i: word_vovel[i]}
            max = word_vovel[i]
        if word_vovel[i] == max:
            longest[i] = word_vovel[i]
    for i in longest.keys():
        word = word + i + ' ' + str(longest[i]) + '\n'
    return word



word_vovel = out_words(text)

words = {a: vovel(a) for a in word_vovel}

word = find_vovels(words)

raw_input('Enter eny key to find word with max number of vovels')
print word
raw_input()


