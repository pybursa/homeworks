y = [3,7,12]
z = [3,7,12,7]

def check(a):
    b = []
    if len(a) % 2 ==0:
        for i in range(len(a)):
            x = a[i]
            #print x
            if x % 2 ==0:
                b.append(x)
    else:
        for i in range(len(a)):
            x = a[i]
            #print x
            if x % 2 !=0:
                b.append(x)
    print a, ">>", b

check(y)
check(z)
