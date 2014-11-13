text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta."

print 'original text: ', text

list = text.split(' ')
point = "."
comma = ","
text1 = []

for i in list:
    if point in i:
        i = i.replace('.','')
        i = i[::-1]+'.'
#        print i
        text1.append(i)
    elif comma in i:
        i = i.replace(',','')
        i = i[::-1]+','
#        print i
        text1.append(i)
    elif i.istitle():
        i = i[::-1]
        i = i.capitalize()
#        print i
        text1.append(i)
    else:
        i = i[::-1]
#        print i
        text1.append(i)

text1 = ' '.join(text1)
print ''
print 'modified words: ', text1

list1 = text1.split('.')
text2 = []

for j in list1:
#    print j
    j = j.strip()
    k = j.split(' ')
    l = []
    for n in reversed(k):
        l.append(n)

    l = " ".join(l)
    l = l.capitalize()
#    print l
    text2.append(l)
#print text2
    
text2 = '. '.join(text2)
text2  = text2.strip()
print ''
print 'second modified:', text2

 
list2 = text2.split('.')
text3  = []
for n in reversed(list2):
    if n != '':
        n = n.strip()
        text3.append(n)

#print '\n', list2
#print '\n', text3
text3 = '. '.join(text3)+'.'
print ''
print 'sentence modified:', text3

