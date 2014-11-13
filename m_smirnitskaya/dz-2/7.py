start = [6, 3, 45, 67, 2, 3, 5, 8, 3, 67, 34, 56, 3, 5, 24, 54, 2453, 5, 0]
print "Input: ", start
l = start
l.sort()

n = -1
for i in reversed(range(0,(len(l)))):
	if l[i-1] % 2 == 0:
		l.insert(len(l), (l[i-1]))
		n = n - 1
		del l[i-1]

print "Output: ", l
if start is l:
	print "True. The same object."