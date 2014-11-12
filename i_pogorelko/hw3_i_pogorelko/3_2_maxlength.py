text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

text = text.replace('.','')
text = text.split(' ')

maxlength = 0
longword = []

for i in text:
    count = len(i)
    print "length of ", i, "= ", count
    if count > maxlength:
        maxlength = count
        longword = [i]
    elif count == maxlength:
        longword = longword + [i]

print ""
print "max length is: ", maxlength
print "the words that have this length: ", ', '.join(longword)
