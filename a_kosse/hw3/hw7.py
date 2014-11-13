#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import input_text

if __name__ == "__main__":
    in_text = input_text()
    in_list = list(in_text)
    out_list = []
    count = 2
    for i in range(len(in_list)):
        if in_list[i].isalpha():
            count += 1
        else:
            if i - count < 0:
                out_list.extend(in_list[i-1::-1])
                out_list.extend(in_list[i])
            else:
                out_list.extend(in_list[i-1:(i-count):-1])
            count = 2
    if count > 2:
        out_list.extend(in_list[:(len(in_list)-count):-1])


    for i in range(len(in_list)):
        if in_list[i].isalpha():
            if in_list[i].isupper():
                out_list[i] = out_list[i].upper()
            else:
                out_list[i] = out_list[i].lower()
        else:
            out_list[i] = in_list[i]



    print ''.join(out_list)
