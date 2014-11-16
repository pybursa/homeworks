"""
Homework 4, task 1
Count percentage of each letter in a string
"""

__author__ = "Elena Sharovar"
__date__ = '2014-11-16'

def percentage_1(s):
    result = {}

    for char in s:
        if char.isalnum():
            lowChar = char.lower()
            if (lowChar in result):
                result[lowChar] += 1.0
            else:
                result[lowChar] = 1.0

    textLength = sum(result.values())

    for key in result.keys():
        result[key] = round(100 * result[key] / textLength, 1)

    return result

def percentage_2(s):
    return percentage_1(s)