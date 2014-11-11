#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, \
consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta.'


def rev(data):
    result = ''
    data = data.split('.')

    for p in data:
        p = p.strip()
        s = p.split(' ')
        temp = []

        for i in s:
            i = i.strip('.,;!?')
            i = i[::-1]

            if len(i) == 0:
                continue

            temp.append(i)

        if not temp:
            continue

        temp.reverse()

        result = ' '.join(temp) + '. ' + result
        temp = []

    i.strip(result)
    return result

if __name__ == '__main__':
    print rev(text)
