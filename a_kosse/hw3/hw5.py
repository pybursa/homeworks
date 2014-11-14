#!/usr/bin/env python
# -*- coding: utf-8 -*-
def input_num():
    while True:
        num = raw_input('Vvedite chislo: ')
        if num.isdigit():
            return num
        else:
            print "chto-to ne tak, povtorite esche raz!"

if __name__ == "__main__":
    in_list = list(input_num())
    result = 0
    for i in in_list:
        result = result - (- int(i))
    print "Summa:", result
