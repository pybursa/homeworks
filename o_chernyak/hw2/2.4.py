l = [4, 5, 6, 7]
i = 0

while i < len(l):
    if (len(l)%2) == 0:
        if i%2 != 0:
            l.remove(l[i])
    else:
        if i%2 == 0:
            l.remove(l[i])
    i += 1    
print l
