t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
print t[2::3]
count = 0
new = []
for i in t:
    count += 1
    try:
        if(count%3 == 0):
            new.append(i)
    except TypeError:
            pass
print new


