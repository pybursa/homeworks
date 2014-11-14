a = [[1],[4,8],[6,3,7],[1,3]]
b = []
for i in a:
#    print i
    if type(i).__name__ == 'list':
        for j in i:
            b.append(j)
    else:
        b.append(i)        
print b
