# -*- coding: utf-8 -*-
_counter = 0
def myfunction(mystring, mysubstring):
    if(mysubstring in mystring):
        global _counter
        _counter += 1
        start = mystring.find(mysubstring)
        myfunction(mystring[start+1:], mysubstring)
    else:
        print "Результат -> " +  str(_counter)
        return False

myfunction("wowhatamanwowowpalehche", "wow")
