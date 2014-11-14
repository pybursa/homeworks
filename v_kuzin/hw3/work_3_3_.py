#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 3. 3
# 
print '----------------------------------------------------'

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
 Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, \
 consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. \
 Cras ultricies ligula sed magna dictum porta.'


print 'INPUT: ', text


# разделение на предложения & revers
def work_text(input_text):
	sentance = ''
	sentances = []
	
	for i in input_text:
		if i != '.':
			sentance = sentance + i
		else:
			sentance = sentance + i
			sentances.append(sentance)
			sentance = ''
	sentances.reverse()
			
	return sentances

# разделение предложения на слова и реверс

def work_sentance(input_sentance):
	word = ''
	words = []
	input_sentance = input_sentance.lstrip()

	for i in input_sentance:
		
		if i != '.' and i != ' ':
			
			word = word + i
			
		if i == '.' or i == ' ':
			words.append(word)
			word = ''
		

	words.reverse()
	len_sentanse = len(words)
	sentance = ''
	for i in words:                                       # reverse
				
		if i == words[len_sentanse-1]:
			sentance = sentance + i[::-1] + '.'
		else:
			sentance = sentance + i[::-1] + ' '
			
	return sentance

reverse_text = work_text(text)  


result = ''
for i in reverse_text:
	result = result + work_sentance(i) + ' '
    
print 'RESULT: ', result


