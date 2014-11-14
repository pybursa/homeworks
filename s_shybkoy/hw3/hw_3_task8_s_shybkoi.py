# -*- coding: utf-8 -*-
#hw 3/ task8 / Sergei Shybkoi

def find_a(txt):
    txt = str(txt)
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    txt = txt.lower().split('a')
    j = 0
    for i, v in enumerate(txt):
        if i == 0 or (len(txt[i-1]) == 0 or len(txt[i]) == 0):
            continue
        if txt[i-1][-1] in cons and txt[i][0] in cons:
            j += 1
    print "Amount 'a' in text is: ", j

t = "Cras ultricies ligula sed magna dictum porta. " \
    "Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. " \
    "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; " \
    "Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. " \
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, " \
    "consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
    "Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, " \
    "elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh."

find_a(t)

