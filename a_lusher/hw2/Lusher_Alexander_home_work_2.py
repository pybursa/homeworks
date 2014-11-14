#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Assignment N 01
#
def multiplier(my_list):
	# check if this is a list
	squares=[x**2 for x in my_list]
	return squares

# Assignment N 02
#
def symmetry(s):
	# check if this is a string
	_length=len(s)
	for i in range(_length):
		if s[i]<>s[_length-1-i]:
			return False
		else:
			continue
	return True

# Assignment N 03
#
def divide_by_three(my_list):
    mod_dict={}
    # check if this is a list
    for x in my_list:
        if x % 3 == 0:
            mod_dict.setdefault(x,(True))
        else:
	    mod_dict.setdefault(x,(False))
    return mod_dict

# Assignment N 04
#
def odd_or_even(my_list):
	# check if this is a list
	sorted_list=[]
	_length=len(my_list)
	if _length%2==0:
		for x in my_list:
			if x%2==0:
				sorted_list.append(x)
	else:
		for x in my_list:
			if x%2<>0:
				sorted_list.append(x)
	return sorted_list

# Assignment N 05
#
def separator(my_list):
	# check if this is a list
	sorted_odd_list=[]
	sorted_even_list=[]
	for x in my_list:
		if x%2==0:
			sorted_even_list.append(x)
		else:
			sorted_odd_list.append(x)
	return sorted(sorted_odd_list)+sorted(sorted_even_list, reverse=True)


if __name__ == '__main__':
	# Mandatory Assignments
	assert multiplier([1,2,3])==[1,4,9]
	assert symmetry("abba")==True
	assert symmetry("joke")==False
	assert divide_by_three([3,7,12])=={3:True, 12:True, 7:False}
	assert odd_or_even([3,7,12])==[3,7]
	assert odd_or_even([3,7,12,7])==[12]
	assert separator([1,4,8,6,3,7,1])==[1,1,3,7,8,6,4]

	print "OK"


