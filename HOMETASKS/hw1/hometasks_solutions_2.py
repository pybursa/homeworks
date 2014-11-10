#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 2: подсчет гласных.
def vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string:
        if letter.lower() in vowels:
            count += 1
    return count


if __name__ == "__main__":
    assert vowels("hApPyHalLOweEn!") == 5
    print "Ok!"
