# -*- coding: utf-8 -*-
#hw 3/ task7 / Sergei Shybkoi

def reverse_txt(txt):
    txt = txt.lower().split('.')[::-1]
    txt = [i[::-1].capitalize().strip() for i in txt if i != '']
    for i, c in enumerate(txt):
        if ',' in c:
            l = c.split(',')
            res = l[0]
            for j in range(len(l)):
                if j > 0:
                    if l[j].find(' ') > 0:
                        l1 = l[j][:l[j].find(' '):]
                        l2 = l[j].replace(l1, l1+',')
                    else:
                        l2 = ', ' + l[j]
                    res += l2
            txt[i] = res
    res = '. '.join(txt)
    return res

t = "Lorem, ipsum dolor sit amet, consectetur adipiscing, elit. " \
    "Nulla quis lorem ut libero malesuada feugiat. " \
    "Lorem ipsum dolor sit, amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. " \
    "Cras ultricies ligula sed magna dictum porta."

print reverse_txt(t)

