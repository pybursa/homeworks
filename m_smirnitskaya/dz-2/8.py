t = (6, 7, 3, 4, 5, 23, 56, 56, 45, 4, 3, 2)
print "Input: ", t
n = len(t)
l = []
for i in range(0, n-1, 2):
    if i != n:
	    l.append((t[i], t[i+1]))
if n % 2 != 0:
	l.append((t[-1], ))

print "Output: ", tuple(l)

