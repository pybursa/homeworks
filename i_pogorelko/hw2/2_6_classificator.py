x = {'a': 1, 3: [1,5], 'e': 'abc', '6': []}
y = x.values()
d = {}
for i in y:
    z = type(i).__name__
#    print z
    if z in d :
        d[z] += 1
    else:
        d[z] = 1
print d


