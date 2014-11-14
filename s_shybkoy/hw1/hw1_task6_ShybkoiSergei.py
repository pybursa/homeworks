# -*- coding: utf-8 -*-
#hw 1/ task6/ Sergei Shybkoi

a = 3
b = 'asd'

if type(a) == type(b) == int:
    if a > b:
        print u"больше"
    elif a < b:
        print u"меньше"
    else:
        print u"равны"
if type(a) == str or type(b) == str:
    print u"получена строка"