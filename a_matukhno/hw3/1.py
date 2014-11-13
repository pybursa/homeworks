# -*- coding: utf-8 -*-
"""
Задание 1: И снова гласные.
УСЛОВИЕ:
Посчитать количество гласных в каждом слове текста.
Вывести максимальное количество гласных в одном слове.
Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
Гласные: A, E, I, O, U, Y
"""

s = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non \
nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

test = 'ababagagamaga'

def hw3(input_string):
    words = input_string.split(' ')
    global_count = 0
    for word in words:
        word_count = 0
        for letter in word:
            if letter.lower() in 'aeiouy':
                word_count += 1
        if global_count < word_count:
            global_count = word_count
    return global_count

if __name__ == '__main__':
    print hw3(s)
    print hw3(test)