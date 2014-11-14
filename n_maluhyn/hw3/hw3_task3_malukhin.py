#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание 3: Реверс'em!
#
# УСЛОВИЕ:
# Изменить в тексте порядок следования:
# - букв в словах;
# - слов в предложениях;
# - предложений в тексте.
# Вывести модифицированный текст.
#
# Текст:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta.


def largest_words(sentence):
    sentence = sentence[0:len(sentence)-1]
    sentence_seq = sentence.split('. ')
    sentence_seq = sentence_seq[::-1]
    reversed_text = ''
    for (s_sent, sent) in enumerate(sentence_seq):

        sent = sent.split(' ')
        sent = sent[::-1]
        reversed_sent = ''
        for (s, word) in enumerate(sent):
            word = word[::-1]
            if word[0] == ',':
                comma = ','
                word = word[1:] + comma

            reversed_sent += word
            if s+1 != len(sent):
                reversed_sent += ' '
            reversed_sent = reversed_sent.capitalize()
        reversed_text += reversed_sent
        if s_sent+1 != len(sentence_seq):
            reversed_text += '. '
    reversed_text += '.'
    print reversed_text

t =  'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta.'
print largest_words(t)
