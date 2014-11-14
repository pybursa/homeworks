#!/usr/bin/env python
# -*- coding: utf-8 -*-

def prostoe (num):
    for i in range(2,(num / 2) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(2,10000):
        if prostoe(i):
            print i


# небходимо вывести 10000 простых чисел, а не все простые в ряде до 10000
