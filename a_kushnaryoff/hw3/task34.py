__author__ = 'alex'

import os
import sys


def task3_4():
    def printing_doc(mod):
        array_for_doc = [mod.__name__ + "." + i + '.__doc__' for i in dir(mod) if i.islower()]
        for i, j in enumerate(array_for_doc):
            print j.replace('__doc__', ''), eval(j)
            print "----------------------------------------------------------"
    printing_doc(sys)
    printing_doc(os)


task3_4()