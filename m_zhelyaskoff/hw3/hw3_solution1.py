#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import calculate_vowels


def main():
    print "\n\n___ Задание 1: И снова гласные " + "_"*15

    text = "Proin eget tortor risus. Cras ultricies ligula\
sed magna dictum porta. Proin eget tortor\
risus. Curabitur non nulla sit amet nisl tempus\
convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

    print 'Input text:\n', text
    result_dict = calculate_vowels(text)
    print "Results:"
    print "   Number of vowels in each word:\n", result_dict
    print "   The max number of vowels in a word:", max(result_dict.values())


if __name__ == '__main__':
    main()


