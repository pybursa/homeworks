#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import a_counter


def main():
    print "\n\n___ Задание 7: Реверс'em all! " + "_"*15

    text = "Cras ultricies ligula sed magna dictum porta. \
Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. \
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere \
cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, \
ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur \
adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, \
pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, \
consectetur adipiscing elit. Sed porttitor lectus nibh."

    print '=== Input text ===\n', text
    result = a_counter(text)
    print '\n=== Result: ==='
    print 'Number of characters "a" surrounded by consonants: ', result


if __name__ == '__main__':
    main()
