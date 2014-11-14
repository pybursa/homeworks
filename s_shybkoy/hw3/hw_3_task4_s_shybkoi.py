# -*- coding: utf-8 -*-
#hw 3/ task4/ Sergei Shybkoi

import os
import sys

def get_doc_func(modul):

    try:
        for i in dir(modul):
            x = 'if type(' + modul.__name__ + '.' + i + ').__name__ in ["function", "builtin_function_or_method"]  and' \
                                                        ' ' + modul.__name__ + '.' + i + '.__doc__ != None:\n'\
                '    print ' + modul.__name__ + '.' + i + '.__doc__'
            exec x
    except AttributeError:
        print "Wrong modul name!"
    print '******************************************************************'

get_doc_func(os)
get_doc_func(sys)



