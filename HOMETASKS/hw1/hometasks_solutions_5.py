#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 5: определение типа.
def typer(obj):
    return type(obj).__name__


if __name__ == "__main__":
    assert typer("string") == "str"
    assert typer(777) == "int"
    assert typer(typer) == "function"
    assert typer({}) == "dict"
    print "Ok!"
