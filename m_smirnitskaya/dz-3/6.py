n = 1
j = 0
count = 0
pr_ch = []
while count <= 10000:
	n += 1
	j = 0

	for i in range(2, 10):
		if n % i != 0:
		    j += 1
		if n == i:
			j += 1
	if j == 8:
	    pr_ch.append(n)
	    count += 1

print pr_ch
	

    