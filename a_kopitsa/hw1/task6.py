# -*- coding: utf-8 -*-
def myfunction(a, b):
    if(a.isalpha() and b.isalpha()):
        print "Получены строки"
        if (len(a) > len(b)):
            print "Строка А больше Б"
        else:
            print "Строка Б больше А"
    else:
        if(a.isdigit() and b.isdigit()):
            print "Получены числа"
            if (a > b):
                print "Число А больше Б"
            else:
                print "Число Б больше А"
        else:
            print "Значения имеют разные типы"


myfunction("dfsdfsd", "4")
myfunction("dfsdfsd", "ty")
myfunction("53", "4")
