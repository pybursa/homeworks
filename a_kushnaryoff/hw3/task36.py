__author__ = 'alex'


import math


def task3_6():
    def primes(num):
        ar = set(range(2, num))
        for i in range(2, int(math.sqrt(num))):
            if i in ar:
                ar -= set(range(2 * i, num, i))
            return ar

    print list(primes(10000))


task3_6()