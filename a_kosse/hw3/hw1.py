#!/usr/bin/env python
# -*- coding: utf-8 -*-
def count_glasnie(word):

    low_word = word.lower()
    count = 0
    for i in low_word:
        if i in "aeiouy":
            count += 1
    return count

from utils import input_text

if __name__ == "__main__":

    in_text = input_text()
    input_list = in_text.split(' ')
    max_glassnie = 0
    for i in input_list:
        temp_counter = count_glasnie(i)
        if temp_counter > max_glassnie:
            max_glassnie = temp_counter

    print 'Maximum number of vowels:', max_glassnie

