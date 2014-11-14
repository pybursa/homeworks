#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import sort_text_by_length


def main():
    print "\n\n___ Задание 2: Самое длинное слово " + "_"*15

    text = "Proin eget tortor risus. Cras ultricies ligula\
sed magna dictum porta. Proin eget tortor\
risus. Curabitur non nulla sit amet nisl tempus\
convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

    print 'Input text:\n', text
    string = text.replace('.', '') #delete points
    string = string.replace(',', '') #delete commas
    sorrted_words = sort_text_by_length(string)

    longest_word = sorrted_words[0]
    longest_words_list = []
    longest_words_list.append(longest_word)

    print "\nLongest words:"
    print "    ", longest_word
    for word in sorrted_words:
        if len(word) < len(longest_word): continue
        if word in longest_words_list: continue
        print "    ", word


if __name__ == '__main__':
    main()
