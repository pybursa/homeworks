# -*- coding: cp1251 -*-
"""Задание 2: Самое длинное слово.


УСЛОВИЕ:
Найти слово максимальной длины в тексте.
Вывести это слово. Если таких слов несколько - вывести все.


Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.
Proin eget tortor risus.
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.
Donec rutrum congue leo eget malesuada.

"""

text = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.
Proin eget tortor risus.
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.
Donec rutrum congue leo eget malesuada."""


def out_words(words):
    import string

    words = words.lower()
    etalon = string.ascii_lowercase + " '"
    words_copy = ''
    for w in words:
        if w in etalon:
            words_copy = words_copy + w
        elif words_copy[-1] != ' ':
            words_copy = words_copy + " "

    words = words_copy.split()

    return words

def longest_word(word):
    max = 0
    out = ''
    longest = {}
    company = lambda y, x: y +'\n' + x

    for i in xrange(len(word)):
        if len(word[i]) > max:
            longest.clear()
            longest[word[i]] = None
            max = len(word[i])
        elif len(word[i]) == max:
           longest[word[i]] = None

    for i in longest.keys():
        out = out + i + '\n'


    return out


def main(in_text):
    out = longest_word(out_words(in_text))
    return out



print text, '\n \n', 'A longest word in this text is:\n\n', main(text)
#raw_input()

