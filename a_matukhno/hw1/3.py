# -*- coding: utf-8 -*-

input_string = 'wowhatamanwowowpalehche'


def findall(entered_string):
    count = 0
    for i in range(entered_string.__len__()-1):
        if entered_string.find('wow', i, entered_string.__len__()-1) == i:
            count += 1
    return count

print findall(input_string)