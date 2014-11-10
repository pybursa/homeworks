#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 1: ambulance
def slice_reverse(string):
    return string[::-1]


def list_reverse(string):
    L = list(string)
    L.reverse()
    return "".join(L)


def reversed_fn(string):
    return "".join(reversed(list(string)))


def list_manual_reverse(string):
    result = []
    for letter in string:
        result.insert(0, letter)
    return "".join(result)


if __name__ == "__main__":
    assert slice_reverse("ambulance") == "ecnalubma"
    assert list_reverse("ambulance") == "ecnalubma"
    assert reversed_fn("ambulance") == "ecnalubma"
    assert list_manual_reverse("ambulance") == "ecnalubma"
    print "Ok!"
