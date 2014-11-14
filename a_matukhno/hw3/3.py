# -*- coding: utf-8 -*-

"""
Задание 3: Реверс'em!
УСЛОВИЕ:
Изменить в тексте порядок следования:
- букв в словах;
- слов в предложениях;
- предложений в тексте.
Вывести модифицированный текст.
Текст:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum
dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada.
Cras ultricies ligula sed magna dictum porta.
"""

s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem \
ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras \
ultricies ligula sed magna dictum porta."


def hw3(input_string):
    print input_string
    input_string = sent_revert(input_string)
    return input_string


def sent_revert(input_string):
    sent_list = input_string.split('.')
    sent_list.reverse()

    for i, sentence in enumerate(sent_list):
        sent_list[i] = words_revert(sentence) + '. '

    input_string = ''.join(sent_list)
    input_string = input_string.replace('  ', ' ')
    return input_string


def words_revert(input_string):
    words = input_string.split(' ')
    words.reverse()
    for i, word in enumerate(words):
        words[i] = letters_revert(word)

    input_string = ' '.join(words)
    return input_string


def letters_revert(input_string):
    input_string = input_string[::-1]
    return input_string


if __name__ == '__main__':
    print hw3(s)