#!usr/bin/python

#my_string=raw_input("Please enter a string: ")
my_string="wowwhatamanwowowpalehche"
my_counter=0
i=0
while i<(len(my_string)-2):
	if my_string[i]=="w" and my_string[i+1]=="o" and my_string[i+2]=="w":
		my_counter+=1
	i+=1
print my_counter

