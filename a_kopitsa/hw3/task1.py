__author__ = 'andrey'

text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. " \
       "Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada"
volwes = "A, E, I, O, U, Y"
count = 0
countw = 0
maxvolwes = 0
for i in text.split(" "):
    countw += 1
    for a in i:
        if a.upper() in list(volwes):
            count += 1
    if maxvolwes <= count:
        maxvolwes = count
    count = 0
print "Max volwes: " + str(maxvolwes)
