#!/usr/bin/python
# -*- coding: utf-8 -*- 
#

def add(x, y):
	a=1
	while a>0:
		a = x & y
		b =  x ^ y
		x = b
		y = a << 1
	return b

def vowel_count(word):
	vowels_counter = 0
	for letter in word:
        	if letter.isalpha():
            		if letter.upper() in 'AEIOUY':
                		vowels_counter += 1
	return vowels_counter

if __name__ == '__main__':

	# Assignment N 1
	text="Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
	
	list=text.split()
	max_vowel_number=0
	for i in range(0,len(list)-1):
		print "word=",list[i],"		number of vowels",vowel_count(list[i])	
		if  vowel_count(list[i])>max_vowel_number:
			max_vowel_number=vowel_count(list[i])
	print "Maximum number of vowels is",max_vowel_number

	# Assignment N 2

	text="Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
	
	list=text.split()
	length=len(list[0])
	words=[]
	words.append(list[0])
	for i in range(1,len(list)-1):
		if length<len(list[i]):
			length=len(list[i])
			words[:] = []
			words.append(list[i])
		elif length==len(list[i]):
			words.append(list[i])
	print "maximum length=",length,"words are",words

	# Assignment N 3
	text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta."	
	list=text.split()
	i=len(text)-1
	mirrored_text=''
	while i>=0:
		mirrored_text=mirrored_text+(text[i])
		i-=1
	print mirrored_text

	# Assignment N 4
	import os
	content=dir(os)
	content_len=len(content)
	for k in range(0,content_len-1):
		s="os"+"."+content[k]+".__doc__"
		print(eval(s))

	import sys
	content=dir(sys)
	content_len=len(content)
	for k in range(0,content_len-1):
		s="sys"+"."+content[k]+".__doc__"
		print(eval(s))


	# Assignment N 5
	input=12345

	a=str(input)
	str_len=len(a)
	i=0
	total=int(a[i])
	while i<str_len-1:
		total=add(total,int(a[add(i,1)]))
		i=add(i,1)
	print total
	

