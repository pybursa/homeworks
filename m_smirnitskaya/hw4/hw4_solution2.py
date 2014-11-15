# -*- coding: utf8 -*-

u"""
ДЗ №4
Решение задачи №2 - Послесловие...
Условие:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, 
если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине (исключение 
первое слово),
и в конце нужно добавить троеточие ("...").

Пример:
text = "Proin eget tortor risus."
limit = 24
output = "Proin eget tortor risus."
limit = 23
output = "Proin eget tortor..."
limit = 13
output = "Proin eget..."
limit = 6
output = "Pro..."
"""

def solution2(st, n=5):
    i = n
    l = st.split(" ")
    if n < len(l[0]):
        return st[0:n] + '...'
    elif n > len(st):
        return str(st)  
        exit
    elif st[n-1] == ' ':
        return st[0:n-1] + '...'
    else:
        while st[i] != ' ':
            i -= 1
        return st[0:i] + '...'

