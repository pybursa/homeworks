#!/usr/bin/env python
# -*- coding: utf-8 -*-


def separator(data):
    data.sort()

    temp = []
    i = 0

    while len(data) > i:
        if data[i] % 2 == 0:
            temp[0:0] = [data[i]]
            data.remove(data[i])
        else:
            i += 1

    for i in temp:
        data.append(i)

    return data

if __name__ == '__main__':
    start_list = [1, 4, 8, 6, 3, 7, 1]
    end_list = separator(start_list)
    print start_list, end_list, start_list is end_list
