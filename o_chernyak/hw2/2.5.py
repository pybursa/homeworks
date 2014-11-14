l = [14, 15, 6, 7]
s = []
r1, r2 = [], []
i = 0

while i < len(l):
    if i%2 != 0:
        r1.extend([l[i]])
    else:
        r2.extend([l[i]])
    i += 1
r1.sort()
r2.sort()
r2.reverse()
s = r1 + r2
print s

