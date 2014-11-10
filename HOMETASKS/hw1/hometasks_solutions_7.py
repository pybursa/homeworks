#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 7: уникальный набор.
def unique_ordered(L):
    result = []
    for item in L:
        if not item in result:
            result.append(item)
    return result


def unique_disordered(L):
    return list(set(L))


if __name__ == "__main__":
    L = ["a", 5, 2, 5, (1, "a"), "a"]
    assert unique_ordered(L) == ["a", 5, 2, (1, "a")]
    assert sorted(unique_disordered(L)) == sorted([2, "a", 5, (1, "a")])
    print "Ok!"
