text = 'aeiouyAEIOUYzxcvbnmSDFGHJa'
r = text.lower().count('a') + text.lower().count('e') + text.lower().count('i') + text.lower().count('o') + text.lower().count('u')
print 'Number of vowels: ' +  str(r)
