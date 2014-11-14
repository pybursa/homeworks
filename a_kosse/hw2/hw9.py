#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ploskiy(in_list):
    result=[]
    for lst in in_list:
      result.extend(lst)
    return result

if __name__ == "__main__":

    print ploskiy([[1],[4,8],[6,3,7],[1,3]])
