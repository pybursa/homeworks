def tuplalize(t):
    arr = []
    for i in xrange(0, len(t), 2):
        arr.append(t[i:i+2])
    return tuple(arr)

print(tuplalize( (1, 4, 8, 6, 3, 7, 1) ))