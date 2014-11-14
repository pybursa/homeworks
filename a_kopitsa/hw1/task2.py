# -*- coding: utf-8 -*-
vowels = 'a', 'e', 'i', 'o', 'u'
mystring = "hApPyHalLOweEn!"
lowermystring = mystring.lower()
count = 0
for x in lowermystring:
    for y in vowels:
        if y == x:
            count += 1
print "Результат -> " + str(count)
