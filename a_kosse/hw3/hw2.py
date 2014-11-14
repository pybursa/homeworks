#!/usr/bin/env python
# -*- coding: utf-8 -*-
def count_letters(word):
    count = 0
    for i in word:
        if i.isalpha():
            count += 1
    return count

from utils import input_text

if __name__ == "__main__":
    in_text = input_text()
    input_list = in_text.split(' ')
    max_letter = [0,]
    for i in input_list:
        temp_counter = count_letters(i)
        if max_letter[0] < temp_counter:
            max_letter = [temp_counter,i]
        elif max_letter[0] == temp_counter:
            max_letter.append(i)
    print max_letter


# Выводит кроме слов максимальную длину, также выводит слова со знаками препинания, если слово последнее в предложении.
