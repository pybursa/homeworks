#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'Proin eget tortor risus. \
Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. \
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. \
Donec rutrum congue leo eget malesuada.'


def max_glas(data):
    g = ('a', 'e', 'i', 'o', 'u', 'y')
    data = data.lower()
    data = data.split(' ')
    result = 0

    for i in data:
        temp = 0
        for s in i:
            if s in g:
                temp += 1
        if temp > result:
            result = temp

    return result

if __name__ == '__main__':
    print 'Максимальное количество гласных в одном слове:', max_glas(text)
