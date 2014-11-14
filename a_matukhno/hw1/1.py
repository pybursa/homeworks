# -*- coding: utf-8 -*-

input_string = 'ecnalubma'


def var1(entered_string):
    return entered_string[::-1]


def var2(entered_string):
    return ''.join(reversed(entered_string))


def var3(entered_string):
    result = ''
    for i in xrange(len(entered_string)-1, -1, -1):
        result += entered_string[i]
    return result


def var4(entered_string):
    result = ''
    for i in range(entered_string.__len__()):
        result += entered_string[-i-1]
    return result

print var1(input_string)
print var2(input_string)
print var3(input_string)
print var4(input_string)



