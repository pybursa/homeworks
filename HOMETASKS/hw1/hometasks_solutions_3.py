#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 3: подстчет вхождений подстроки.
def wower(string):
    wows = 0
    for i in range(1, len(string)-1):
        if string[i-1:i+2] == 'wow':
            wows += 1
    return wows


def flag_wower(string):
    count = 0
    flag = None
    for a in string:
        if a == 'w' and flag != 'o':
            flag = a
        if flag == 'w':
            if a == 'o':
                flag = a
            elif a == 'w':
                pass
            else:
                flag = None
        elif flag == 'o':
            if a == 'w':
                count += 1
                flag = 'w'
            else:
                flag = None
        else:
            flag = None
    return count


if __name__ == "__main__":
    assert wower("wowhatamanwowowpalehche") == 3
    assert flag_wower("wowhatamanwowowpalehche") == 3
    print "Ok!"
