a = (input("Input tuple:  "))
q = []
def f(a):
    for i in range (0, len(a)-2,3):
        q.append(a[i+2])
    return tuple(q)
print f(a)
print type(f(a))
