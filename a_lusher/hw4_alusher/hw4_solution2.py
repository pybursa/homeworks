# -*- coding: utf-8 -*- 

# Assignment #4.2 - An Afterword
# Takes any text and character limit and cuts off all characters beyond that using the following
# rule - entire word unless this is the first one. After the cut-off is done, add '...' after the text
# Examples:
# 	text = "Proin eget tortor risus."
# 	limit = 24
# 		output = "Proin eget tortor risus."
# 	limit = 23
# 		output = "Proin eget tortor..."
# 	limit = 13
# 		output = "Proin eget..."
# 	limit = 6
# 		output = "Pro..."

__author__ = "a_lusher"
__date__ = "2014-11-12"


def cut_off(text, max_characters=-1):
#	This function takes any text and character limit and 
#	cuts off all characters beyond that using the rules described above

	modified_text=text[:max_characters]
	cut_off_char=max_characters-1

	if (max_characters==-1)or(max_characters==len(text)):
		return text

	if (ord(modified_text[cut_off_char])==32):
		return modified_text[:(cut_off_char-2)]+'...'		



	# if the last word is incomplete,then start looking for the first space or end of count
	while (ord(modified_text[cut_off_char])<>32):
		cut_off_char-=1

	if cut_off_char>0:
			return modified_text[:(cut_off_char)]+'...'

	if cut_off_char==0:
		return modified_text[:(cut_off_char-2)]+'...'