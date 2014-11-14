# -*- coding: utf-8 -*-
#hw 3/ task5/ Sergei Shybkoi

def sum_num(lst):
    l = [int(i) for i in lst]
    res = l[0]
    for i, val in enumerate(l):
        if i > 0:
            for j in range(0, 9999, 1):
                if (j - res) == val:
                    res = j
                    break
    return res

num = raw_input("Enter natural number:\n")
while True:
    if num.isdigit():
        print sum_num(num)
        break
    else:
        print "Wrong input data!"
        num = raw_input("Enter natural number:\n")






