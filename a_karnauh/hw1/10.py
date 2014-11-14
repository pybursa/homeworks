y = "yes"
while y == "yes":
	s = raw_input("Please, enter your string: ") 
	a = "aeiou"
	s = s.lower()
	b = 0
	for char in s:
		b += a.count(char)
	print "The string contains", b, "vowels"
	y = raw_input("Continue? (yes/no)")

	if y == "yes":
		print "Hurray!"
	elif y == "no":
		break
	else:
		y = raw_input("Please, enter corrent answer. Continue? (yes/no) ")