l = [9, 12, 15, 7, 5, 8]
d = {}
b = True

for i in range(len(l)):
    if (l[i]%3) == 0:
        b = True
    else:
        b = False
    d.update({l[i]: b})    

print d
