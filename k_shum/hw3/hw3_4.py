#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys


def doc(obj):
    for f in dir(obj):
        if callable(getattr(obj, f)):
            print eval(obj.__name__ + '.' + f + '.__doc__')

if __name__ == '__main__':
    doc(os)
    doc(sys)
