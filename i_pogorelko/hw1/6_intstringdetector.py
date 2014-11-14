A = 67
B = 99

#print type(A)
#print type(B)

if (type(A) is str) or (type(B) is str):
    print "we have a string"
elif A > B:
    print "More"
elif A == B:
    print "Equal"
elif A < B:
    print "Less"
