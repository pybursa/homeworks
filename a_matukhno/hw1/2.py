# -*- coding: utf-8 -*-

input_string = 'hApPyHalLOweEn!'


def count_vowels(entered_string):
    count = 0
    for i in entered_string:
        if i.lower() in 'aeiou':
            count += 1
    return count

print count_vowels(input_string)