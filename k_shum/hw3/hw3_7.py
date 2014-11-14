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
        keys = []

        for k, i in enumerate(s):
            if len(i) == 0:
                continue

            i = i[::-1]
            if i[0] == ',':
                i = i[1:]
                keys.append(k)
            temp.append(i)

        if not temp:
            continue

        temp.reverse()

        for i in keys:
            temp[i] += ','

        p = ' '.join(temp)
        p = p[0].upper() + p[1:].lower()
        result = p + '. ' + result

        temp = []
        keys = []

    i.strip(result)
    return result

if __name__ == '__main__':
    print rev(text)
