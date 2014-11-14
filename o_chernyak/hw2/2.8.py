l = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
k = []
i = 0
while i < (len(l)-1):
    k.append((l[i], l[i+1]))
    i += 2
if len(l)%2 != 0:
    k.append((l[-1], ))
print tuple(k)
