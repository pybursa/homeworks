#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import prime_numbers


def main():
    print "\n\n___ Задание 6: Простые числа " + "_"*15

    max_limit = 10000
    print "max limit:", max_limit
    prime_numbers_list = prime_numbers(max_limit)
    result = ' '.join(prime_numbers_list)
    print result



if __name__ == '__main__':
    main()





