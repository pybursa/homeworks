def allmost_sum(digit):
	result = 0
	power = find_max_power(digit)
	while power != 1:
		result -= digit//power
		digit -= digit//power*power
		power /= 10
	result-= digit
	return 0 - result

def find_max_power(digit):
	power = 1
	while digit//power != 0:
		power *=10
	return power/10



print allmost_sum(456)