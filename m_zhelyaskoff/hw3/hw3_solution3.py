#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    print "\n\n___ Задание 3: Реверс'em! " + "_"*15

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta."

    print 'Input text:\n', text
    characters = list(text)
    characters.reverse()
    reversedtext = ''.join(characters)
    print '\n=== Result text === \n', reversedtext


if __name__ == '__main__':
    main()
