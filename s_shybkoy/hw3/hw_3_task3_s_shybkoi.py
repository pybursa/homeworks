# -*- coding: utf-8 -*-
#hw 3/ task3/ Sergei Shybkoi

def reverse_txt(txt):
    txt = txt.lower().split('.')[::-1]
    txt = [i[::-1].capitalize().replace(' ,', ', ').strip() for i in txt if i != '']
    return '. '.join(txt)

t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
    "Nulla quis lorem ut libero malesuada feugiat. " \
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. " \
    "Cras ultricies ligula sed magna dictum porta."

print reverse_txt(t)

