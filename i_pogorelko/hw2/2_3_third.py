a = [3,7,12]
b = {}
for i in range(len(a)):
    if a[i]%3 == 0:
#        print a[i], a[i]/3.0
        b[a[i]] = True
    else:
#        print a[i], a[i]/3.0
        b[a[i]] = False
        
print b
