__author__ = 'alex'
# -*- coding: utf-8 -*-


def task_6(A, B):
    def compare(a, b):
        if type(a).__name__ == 'str' or type(b).__name__ == 'str':
            print u'получена строка'
        else:
            if a > b:
                print str(a) + u' больше ' + str(b)
            elif a < b:
                print str(a) + u' меньше ' + str(b)
            else:
                print str(a) + u' u '+str(b) + u' равны'
    compare(A, B)


#  A = str  B = int
A = 'string'
B = 5
task_6(A, B)

#  A = int  B = str
A = 5
B = 'string'
task_6(A, B)

#  A > B
A = 5
B = 3
task_6(A, B)

#  A < B
A = 5
B = 10
task_6(A, B)

#  A < B
A = 5
B = 5
task_6(A, B)