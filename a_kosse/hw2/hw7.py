#!/usr/bin/env python
# -*- coding: utf-8 -*-

def separator(in_list):
    chet_list = []
    nechet_list = []
    for i in in_list:
        if i % 2 == 0:
            chet_list.append(i)
        else:
            nechet_list.append(i)
        chet_list.sort()
        chet_list.reverse()
        nechet_list.sort()


    for i in range(len(in_list)):
        in_list.pop(0)

    for i in nechet_list:
        in_list.append(i)
    for i in chet_list:
        in_list.append(i)

    return in_list

if __name__ == "__main__":
    print separator([1,4,8,6,3,7,1])
    start_list = [1,4,8,6,3,7,1]
    end_list = separator(start_list)
    print (start_list is end_list)
