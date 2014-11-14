#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 3. 2
# 
print '----------------------------------------------------'

text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.\
 Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis\
  quis ac lectus. Donec rutrum congue leo eget malesuada'
list_worbs = ['a', 'i', 'e', 'o', 'u'] 


print 'INPUT: ', text

print '----------------------------------------------------'

# разделение текста на слова и запись в список words[]
def count_words(sentanse):
	word = ''
	words = []
	sentanse = sentanse.lower()

	for i in sentanse:
		if i != ' ' and i != '.':
			word = word + i
		else:
			if len(word)!= 0:
				words.append(word)
				word = ''
	return words

#определение максимального количества букв в словах
def count_letters(sort_text):
	letters = []
	letter = 0

	for i in sort_text:
		for n in i:
			letter += 1
				
		letters.append(letter)
		letter = 0
	
	letters.sort()
	letters.reverse()
	max_long = letters[0]	
	
	return max_long

# выбор слов с максимальным количеством букв и печать

def result(words, maximum):
	
	for i in words:
		if len(i) == maximum:
			print '   -', i
	


list_text = count_words(text)               # список с словами

max_digital = count_letters(list_text)      # максимальное число букв   
print 'maximum letters in word: ', max_digital
print 'words with maximum letters: '
result(list_text, max_digital)


print '-------------------------------------------------------'
