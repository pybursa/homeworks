#!/usr/bin/env python
# -*- coding: utf-8 -*-

def razdel(text, razdelitel):
    if razdelitel :
        input_list = text.split(razdelitel)
    else:
        input_list = list(text)

    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip()

    if '' in input_list:
        input_list.remove('')

    input_list.reverse()
    if razdelitel == '.':
        razdelitel = '. '

    print razdelitel.join(input_list),
    input_list.reverse()
    return input_list



from utils import input_text

if __name__ == "__main__":
    in_text = input_text()
    sentence = razdel(in_text,'.')
    print
    print
    word = []
    for i in sentence:
        word.append(razdel(i,' '))
        print'. ',
    print
    print

    for words in word:
        for i in words:
            razdel(i,'')
            #print ' ',
        print '. ',
