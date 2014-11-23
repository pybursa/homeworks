l = [5, 7, 3, 4, 44, 167, 203, 121]
print 'Input:', l
d = {}
for i in l:	
	if i % 3 == 0:
		d[i] = True
	else:
		d[i] = False

print 'Dictionary: ', d