a = [1,4,8,6,3,7,1]
print "input: ",a
b = []
c = []
for i in a:
    if i%2 ==0:
        b.append(i)
    else:
        c.append(i)

b = sorted(b, reverse = True)
c = sorted(c)

print "output: ",c + b
