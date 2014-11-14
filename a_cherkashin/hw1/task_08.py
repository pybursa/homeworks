def slice_1():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
    z = t[2::3]
    return z

def for_2():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
    l = []
    for i in range(2, len(t), 3): 
        l.append(t[i])
    return tuple(l)

print slice_1()
print for_2()
