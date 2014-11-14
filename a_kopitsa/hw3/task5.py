__author__ = 'andrey'

import math
#a = [1, 3, 2]
#print math.fsum(a)

def myfunction(var):
    l = []
    for i in str(var):
        l.append(int(i))
    print int(math.fsum(l))

myfunction(456)
