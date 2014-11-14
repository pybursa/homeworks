#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sim(string):
    strlen = len(string)

    half = strlen / 2

    s1, s2 = string[:half], string[half if strlen % 2 == 0 else half+1:]

    if s1 != s2[::-1]:
        return False

    return True

if __name__ == '__main__':
    print sim("abba")
    print sim("abiba")
    print sim("arbat")
