#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init(x, y, z):
    return min(max(y, x), z)

print init(10,20,15)
print init(10,20,30)
print init(25,20,30)
