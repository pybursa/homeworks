t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
y = list(t)
z = t[2::3]
w = tuple(z)
print "Variant-1:", w

op = []
for i in range(1, len(t), 1):
	if (i + 1) % 3 == 0:
		op.append(t[i])
print "Variant-2:", tuple(op)