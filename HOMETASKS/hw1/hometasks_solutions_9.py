#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 9: XYZ.
def xyz(x, y, z):
    return min(max(x, y), z)


if __name__ == "__main__":
    assert xyz(1, 3, 2) == 2
    assert xyz(1, 1, 1) == 1
    assert xyz(3, 2, 1) == 1
    assert xyz(1, 1, 2) == 1
    print "Ok!"
