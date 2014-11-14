a = [1,4,9]
b = (2,5,10)
print "list_start: ", a
print "tuple_start: ", b
print ""
a2 = []
b2 = []

for i in a:
    a2.append(i**2)
print "list: ", a2

for i in b:
    b2.append(i**2)

tup = tuple(b2)
print "tuple: ", tup
