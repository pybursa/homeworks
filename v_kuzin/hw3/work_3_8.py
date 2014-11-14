#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 3. 8
# подсчет сочетаний двух согласных и одной гласной а в середине
print '----------------------------------------------------'

text = 'Cras ultricies ligula sed magna dictum porta. Vivamus magna justo,\
 lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum primis\
 in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque,\
 auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet,\
 consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit.\
 Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet,\
 consectetur adipiscing elit. Sed porttitor lectus nibh.'
list_worbs = ['a', 'i', 'e', 'o', 'u', 'y'] 
list_sint = [' ', ',', '.']

print 'INPUT: ', text

print '----------------------------------------------------'
print ' "a" между 2-я согласными'

list_worbs = list_worbs + list_sint
result = 0

for i in range(1, len(text)-1):
	if text[i] not in list_worbs and text[i-1] == 'a' and text[i-2] not in list_worbs:
		result += 1

print 'RESULT: ', result

print '-------------------------------------------------------'
