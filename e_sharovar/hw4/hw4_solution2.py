"""
Homework 4, task 2
Ellipsis for a string
"""

__author__ = "Elena Sharovar"
__date__ = '2014-11-16'

def ellipsis_1(text, limit = 0):
    if limit == 0:
        return text
    if len(text) <= limit:
        return text

    splitPoint = limit-3
    if (text[splitPoint] == ' '):
        return text[:splitPoint] + '...'

    wordBorder = text.rfind(' ', 0, splitPoint)
    if (wordBorder == -1):
        return text[:splitPoint] + '...'
    else:
        return text[:wordBorder] + '...'

