#!/usr/bin/env python
# -*- coding: <encoding name> -*-

__author__ = "i_pogorelko"
__email__ = "i.pogorelko@gmail.com"
__date__ = "2014-11-16"

text='Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.\
 Donec rutrum congue leo eget malesuada.'

def percentage_1(text):
    print ''
    print 'input: ', text

    text = text.lower()
    text2 = ''
    for x in text:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            text2 = text2 + x

    d = {}
    m = 0
    for j in text2:
        if d.has_key(j):
            d[j] += 1.0
        else:
            d[j] = 1.0
        m += 1

    for key in d:
        d[key] = float("%.1f" % ((d[key]/m)*100))

    print '\noutput: ', d
    return  d
    
def percentage_2(text):
    return percentage_1(text)

percentage_1(text)
