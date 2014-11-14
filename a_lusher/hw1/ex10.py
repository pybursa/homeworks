#!usr/bin/python

response="yes"

while response=="yes":

	my_string=raw_input("Please enter a string: ")

	my_list="aeiou"
	my_counter=0
	my_string=my_string.lower()

	i=len(my_string)-1
	while i>=0:
		if my_string[i] in my_list:
			my_counter+=1
		i-=1
	print "The total number of vowels is:"
	if my_counter==0:
		print "The string doesn't contain vowels"
	if my_counter>0:
		print "The string contains",my_counter,"vowels"
	
	_continue=""
	while _continue=="":
		_continue=raw_input("Continue?")
		if _continue=="no":
			print "It was nice to count your vowels!"
			response="no"
		if _continue<>"no" and _continue<>"yes":
			print "Please enter the correct answer/ Continue? (yes | no)"
			_continue=""		

 