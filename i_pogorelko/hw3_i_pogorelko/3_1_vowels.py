text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuadai"
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

#print 'text = ', text

text = text.replace('.','')
text = text.split(' ')
maxcount = 0

for i in text:
    count = 0
    for j in i:
        if j in vowels:
#            print j
            count += 1
    print 'count of vowels in ', i, ' = ', count
    if count > maxcount:
        maxcount = count

#print text
print 'maxcount = ', maxcount
#print vowels
