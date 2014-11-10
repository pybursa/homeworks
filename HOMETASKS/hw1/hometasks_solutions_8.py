#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 8: каждый третий.
def thirds(T):
    return T[2::3]


def iter_thirds(T):
    return tuple([item for i, item in enumerate(T, 1) if i % 3 == 0])


if __name__ == "__main__":
    T = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
    print thirds(T)
    print iter_thirds(T)
    assert thirds(T) == (3, 6, 9, 'b')
    print "Ok!"
