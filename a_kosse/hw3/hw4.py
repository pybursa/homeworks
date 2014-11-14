#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_help(module):
    for i in dir(module):
        if '__' not in i:
            print help(i)


import os
import sys
if __name__ == "__main__":
    print_help(os)
    print_help(sys)


# желательно ориентироваться на атрибут объектов __doc__
