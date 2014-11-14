# -*- coding: cp1251 -*-
'''Задание 3: Реверс'em!


УСЛОВИЕ:
Изменить в тексте порядок следования:
- букв в словах;
- слов в предложениях;
- предложений в тексте.
Вывести модифицированный текст.


Текст:
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla quis lorem ut libero malesuada feugiat.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec rutrum congue leo eget malesuada.
Cras ultricies ligula sed magna dictum porta.'''

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta.'

def pred(enter):
    enter = enter.split('.')
    enter.reverse()
    enter.remove('')
    enter = '. '.join(enter) + '.'
    return enter

def word(enter):
    enter = enter.lower()
    enter = enter.split('.')

    for i in range(len(enter[:])):
        word = enter[i].split(' ')
        if '' in word:
            word.remove('')
        word.reverse()
        for w in range(len(word[:])):
            word[w] = letter(word[w])
           # print word
        if '' in word:
            word.remove('')
        word = ' '.join(word)
        word = word.capitalize()
        enter[i] = word


    enter.remove('')
    enter = '. '.join(enter) + '.'
    enter = enter.split(' ,')
    enter = ', '.join(enter)
    return enter

def letter(x):
    y = ''
    for i in reversed(x):
        y = y + i
    return y

print 'Before:\n', text
text = pred(text)
text = word(text)
print '\nAfter:\n', text

