# -*- coding: utf-8 -*-
#hw 3/ task6/ Sergei Shybkoi

def simpl_num(first_num):
    n = 200000
    p = [i for i in range(n)]
    p[1] = 0
    i = 2
    while i < n:
        if p[i] != 0:
            j = i * 2
            while j < n:
                p[j] = 0
                j += i
        i += 1
    j = 1
    for i in p:
        if p[i] != 0:
            if j > first_num:
                break
            print str(j) + ": " + str(p[i])
            j += 1

simpl_num(10000)
