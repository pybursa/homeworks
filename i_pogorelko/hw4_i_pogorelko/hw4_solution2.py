#!/usr/bin/env python
# -*- coding: <encoding name> -*-

__author__ = "i_pogorelko"
__email__ = "i.pogorelko@gmail.com"
__date__ = "2014-11-16"

def countstring(text, limit):
    return text[0:limit]

def ellipsis_1(text,limit=0):
    symbols = [' ']
    lengthstr = text.find(' ',0,len(text))
#    print 'lengthstr: ', lengthstr
#    print 'limit: ', limit

    if limit == 0:
#        print 'text3: ', text
        return text

    if limit >= len(text):
#        print 'text2: ', text
        return text

    if limit <= lengthstr and limit > 3:
        print 'text1: ', countstring(text, (limit - 3)) + "..."
        return countstring(text, limit-3) + "..."
   
    if text[limit] in symbols:
#        print 'test5: ', countstring(text, limit)
        return countstring(text, limit)
    else:
        while True:
            if text[limit] != ' ' and limit > text.find(' ',0,len(text)):
                limit = limit - 1
            else:
                break
#        print 'text4: ', countstring(text, limit) + "..."
        return countstring(text, limit) + "..."

def interactive():
    
    sum = len(text)
    while True:
        limit = raw_input('input limit please:')
    
        if limit.isdigit():
            limit = int(limit)
            if limit > sum:
                print 'out of range'
            else:
                break
        else:
            print 'Not correct. Please input the number'

if __name__ == '__main__':
    text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.\
 Donec rutrum congue leo eget malesuada."
    sum = len(text)
    while True:
        limit = raw_input('input limit please: ')

        if limit.isdigit():
            limit = int(limit)
            if limit > sum:
                print 'out of range'
            else:
                break
        else:
            print 'Not correct. Please input the number'
    print 'result is: ', ellipsis_1(text,limit)
