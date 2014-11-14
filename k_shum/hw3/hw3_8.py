#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'Cras ultricies ligula sed magna dictum porta. \
Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. \
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere \
cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper \
sit amet ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor \
sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere \
blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem \
ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh.'


def aaa(data):
    g = ('a', 'e', 'i', 'o', 'u', 'y')
    data = data.lower()
    data = data.split(' ')
    result = 0

    for i in data:
        i = i.strip('.,;!?')
        l = len(i) - 1

        for k, b in enumerate(i):
            if b != 'a':
                continue

            if k == 0 or k == l:
                continue

            if i[k-1] in g or i[k+1] in g:
                continue

            result += 1

    return result

if __name__ == '__main__':
    print 'Количество букв A:', aaa(text)
