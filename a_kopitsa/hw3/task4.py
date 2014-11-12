__author__ = 'andrey'

import os
import sys

print "Module OS: "
for i in dir(os):
    print help(i)

print "Module SYS: "
for i in dir(sys):
    print help(i)

