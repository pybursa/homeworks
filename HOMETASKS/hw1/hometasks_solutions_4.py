#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 4: упорядоченная подстрока.
def alphabetical(string):
    current = string[0]
    longest = string[0]
    for i in range(1, len(string)):
        if string[i] >= current[-1]:
            current += string[i]
            if len(current) > len(longest):
                longest = current
        else:
            current = string[i]
    return longest


if __name__ == "__main__":
    assert alphabetical("sabrrtuwacaddabra") == "abrrtuw"
    print "Ok!"
