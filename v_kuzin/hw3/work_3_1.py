#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 3. 1
# 
print '----------------------------------------------------'

text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.\
 Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis\
  quis ac lectus. Donec rutrum congue leo eget malesuada'
list_worbs = ['a', 'i', 'e', 'o', 'u'] 


print 'INPUT: ', text
print '---------------------'
print 'Select: ', list_worbs
print '----------------------------------------------------'

# разделение текста на слова и запись в список words[]
def count_words(sentanse):
	word = []
	words = []
	sentanse = sentanse.lower()

	for i in sentanse:
		if i != ' ' and i != '.':
			word.append(i)
		else:
			if len(word)!= 0:
				words.append(word)
				word = []
	return words

#определение количества гласных, согласно списка, в каждом слове и запись количества в vowels[]
def count_vowels(sort_text, list_vowels):
	vowels = []
	vowel = 0

	for i in sort_text:
		for n in i:
			if n in list_vowels:
				vowel += 1
				
		vowels.append(vowel)
		vowel = 0
	return vowels


# определение общего количества глассных
def result_all_vawoles(list_digit):
	summa = 0
	for i in list_digit:
		summa = summa + 1
	return summa


list_text = count_words(text)

vowels_all = count_vowels(list_text, list_worbs)

result = result_all_vawoles(vowels_all)

vowels_all.sort()
vowels_all.reverse()

max_digit = vowels_all[0]


#print 'result: ', count_words(text)
#print count_vowels(list_text, list_worbs)

print 'Vowoles: ', result

print 'max: ', max_digit
