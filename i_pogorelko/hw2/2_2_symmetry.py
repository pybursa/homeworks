#a = "abba"
a = raw_input("please input your word: ")
b  = a[::-1]

f = 0

for i in range(len(a)):
    if a[i] != b[i]:
        f = 1

if f == 1:
    print "unsymmetric: ", False
else:
    print "symmetric: ", True
