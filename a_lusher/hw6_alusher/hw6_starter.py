#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script runs Home Assignment 6

__author__ = "a_lusher"
__date__ = "2014-11-17"

from hw6_solution1 import modifier

def runner():
    # Runs all tasks	
    print "Modifying file..."
    modifier("data.csv")
    print "Modified successfully!"

if __name__ == '__main__':
    runner()