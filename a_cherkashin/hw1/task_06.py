# -*- coding: utf-8 -*-

def compare(a, b):
    if type(a).__name__ == 'str' or type(b).__name__ == 'str':
        print u'получена строка'
    else:
        if a > b:
            print str(a) + u' больше ' + str(b)
        elif a < b:
            print str(a) + u' меньше ' + str(b)
        else:
            print str(a) + u' u '+str(b) + u' равны'
a = raw_input(u'Строка или число: ')
b = raw_input(u'Строка или число: ')
compare(a,b)

