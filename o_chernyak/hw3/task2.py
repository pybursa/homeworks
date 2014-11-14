# -*- coding: utf-8 -*-
long_word = " "
longest_words = []
text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada1. malesuada2."

for i in (text.split(' ')):
    print i, len(i)
    if len(i) >= len(long_word):
        long_word = i
        longest_words.extend([long_word])

# Этот код выдавал максимумальную длину слова - 9. Что бы получить больше 9, пришлось добавить key=len. Можно это объяснить на ближайшем семинаре пожалуйста
#    for j in longest_words:
#        if len(j) < len(max(longest_words)):
#            longest_words.pop(longest_words.index(j))
    
    for j in longest_words:
        if len(j) < len(max(longest_words, key=len)):
            longest_words.pop(longest_words.index(j))

print "The longest word(s) are:", longest_words

