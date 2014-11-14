#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import reverse_text

def main():
    print "\n\n___ Задание 7: Реверс'em all! " + "_"*15

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta."

    print '=== Input text ===\n', text
    result_text = reverse_text(text)
    print '\n=== Result text === \n', result_text


if __name__ == '__main__':
    main()
