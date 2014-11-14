# -*- coding: utf-8 -*-
def myfunction(var):
    print type(var).__name__

myfunction(666)
myfunction("666")
myfunction(myfunction)
