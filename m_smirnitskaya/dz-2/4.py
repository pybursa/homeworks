lnew = []
def sort(l):
	lnew = []
	if s % 2 == 0:
	    for i, k in enumerate(l):
		    if k % 2 == 0:
			    lnew.append(l[i])
	else:
	    for i, k in enumerate(l):
		    if k % 2 != 0:
			    lnew.append(l[i])
	print lnew




l1 = [5, 7, 12, 5, 6, 9, 156, 477, 45, 23, 4, 6, 2, 78, 9, 6, 3]
print "Input: ", l1
s = len(l1)
print "The number of elements: ", s
sort(l1)
print ("------------------------------------")
l2 = [6, 7, 2, 45, 23, 5, 2, 8, 566, 3, 6, 4]
print "Input: ", l2
s = len(l2)
print "The number of elements: ", s
sort(l2)