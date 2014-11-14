def is_prime(digit):
	if digit < 2:
		return False
	i = 2 
	while i <= digit / 2:
		if digit % i == 0:
			return False
		i += 1
	return True


count = 0
number = 0
while count < 10000:
	if is_prime(number):
		print "%i - %i" % (count+1, number)
		count += 1
		number += 1
	else:
		number += 1
