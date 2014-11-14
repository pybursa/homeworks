#!/usr/bin/env python
# -*- coding: utf-8 -*-

def typer(incom):
    a = type(incom)
    a = str(a)
    in_list = a.split("'")
    return in_list[1]

def classificator(in_list):
    result = {}
    for i in in_list:
        type_str = typer(in_list[i])
        if result.has_key(type_str):
            result[type_str] += 1
        else:
            result[type_str] = 1
    return result


if __name__ == "__main__":

    print classificator({'a': 1, 3: [1,5], 'e': 'abc', '6': []})

