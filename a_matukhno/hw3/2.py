# -*- coding: utf-8 -*-

"""
Задание 2: Самое длинное слово.
УСЛОВИЕ:
Найти слово максимальной длины в тексте.
Вывести это слово. Если таких слов несколько - вывести все.
Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit
 amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
"""

s = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non \
nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."


def hw3(input_string):
    max_length = 0
    export_list = []
    input_string = input_string.replace('.', '')
    words = input_string.split(' ')
    for word in words:
        if word.__len__() > max_length:
            max_length = word.__len__()
            export_list = []
            export_list.append(word)
        elif word.__len__() == max_length:
            export_list.append(word)
    return export_list


if __name__ == '__main__':
    print hw3(s)