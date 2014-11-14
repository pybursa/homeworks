a = (1,4,8,6,3,7,1)
print "intput: ", a
b = ()
for i in range((len(a)+1)/2):
    if len(a)/2 > i:
            bi = (int(a[i*2]), int(a[i*2+1]))
            #print "list for i= ", bi
            w  = (bi,)
            b = b+w
            #print "concat: ", b
    else:
            bi = (int(a[i*2]),)
            #print "list for i= ", bi
            w  = (bi,)
            b = b+w
            print "output: ", b
