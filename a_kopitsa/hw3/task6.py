__author__ = 'andrey'

from math import sqrt
data = 10000
spisok = []
for i in xrange(2, data + 1):
    for j in spisok:
        if j > int((sqrt(i)) + 1):
            spisok.append(i)
            break
        if (i % j == 0):
            break
    else:
        spisok.append(i)
print spisok
