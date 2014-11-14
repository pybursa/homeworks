#!usr/bin/python

#my_string=raw_input("Please enter a string: ")
my_string="hAppY HAllOweeN!"


my_list="aeiou"
my_counter=0
my_string=my_string.lower()

i=len(my_string)-1
while i>=0:
	if my_string[i] in my_list:
		my_counter+=1
	i-=1
print "The total number of vowels is:"
print my_counter


 