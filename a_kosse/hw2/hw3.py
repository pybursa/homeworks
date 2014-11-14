#!/usr/bin/env python
# -*- coding: utf-8 -*-
def tridelenie(in_list):
    result = {}
    for i in in_list:
            result[i] = i % 3 == 0
    return result


if __name__ == "__main__":
    print tridelenie([3,7,12])

