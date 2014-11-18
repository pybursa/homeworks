l = [6, 3, 45, 67, 2, 3, 5, 8, 3, 67, 34]
print "Input: ", l
lc = []
ln = []

for i, k in enumerate(l):
    if k % 2 == 0:
	    lc.append(l[i])
    if k % 2 != 0:
	    ln.append(l[i])

ln.sort()
lc.sort()
lc.reverse()
fin = ln + lc
print "Output: ", fin