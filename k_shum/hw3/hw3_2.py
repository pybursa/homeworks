#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'Proin eget tortor risus. \
Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. \
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. \
Donec rutrum congue leo eget malesuada.'


def slova(data):
    data = data.split(' ')
    result = []
    temp = 0

    for i in data:
        i = i.strip('.,;!?')
        l = len(i)
        if l > temp:
            result = []
            result.append(i)
            temp = l
        elif l == temp:
            result.append(i)

    return result

if __name__ == '__main__':
    print 'Самые длинные слова:', slova(text)
