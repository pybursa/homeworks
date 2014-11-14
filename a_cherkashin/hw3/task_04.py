import os
import sys
 

def echo_help():
    for lib in (os, sys):
        for func in dir(lib):
            print help(func)

echo_help()
