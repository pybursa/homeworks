# -*- coding: utf-8 -*- 

# Assignment #4.1 - Dictionary of all character occurences in a given text
# Takes any text and returns a dictionary 
# Example: "Abbey">>{'a':1,'b':3,'e':1,'y';1}

__author__ = "a_lusher"
__date__ = "2014-11-12"


def char_counter(string, s):

	# Takes a character and text and finds the number of the character occurences in the string

	if (isinstance(s, str)<>True) or (isinstance(s, str)==True and len(s)>1):
		print "The second argument should be a single character"
		quit()
	if isinstance(string, str)<>True:
		print "The first argument should be a string"
		quit()

	return string.lower().count(s)



def text_analyzer(string):
	
	# Takes text and creates a dictionary with counts for all letters

	from sortedcontainers import SortedDict

	if isinstance(string, str)<>True:
		print "The argument should be a string"
		quit()

	if len(string)==0:
		print "The argument cannot be an empty string"
		quit()


	if len(string)==1:
		return{string.lower(): 100.0}

	dict={}
	total_count=0	
	alphabet="abcdefghijklmnopqrstuvwxyz"

	for i in range (0,len(alphabet)-1):
		count=char_counter(string, alphabet[i])
		if count>0:
			dict.update({alphabet[i]: count})
			total_count+=count


	for key in dict.keys():
		dict[key] = round(float(dict[key])*100/total_count,1)

	return dict


