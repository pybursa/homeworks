a = [2, 3, 7, 7, 6, 2]
if len(a)%2==0:
    print [i%2 == 0 for i in a]
else:
    print [n%2 != 0 for n in a]
