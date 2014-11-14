#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 6

print '*****************************************'

print "Please, enter A: "
a=raw_input()
print "Please, enter B: "
b=raw_input()
# анализ данных
if type(a)==str or type(b)==str:
    print 'get the string', u'(получена строка)'
elif a>b:
    print 'more', u'(больше)'
elif a<b:
    print 'less', u'(меньше)'
else:
    print'equally', u'(равно)'
print '*****************************************'
