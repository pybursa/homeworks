__author__ = 'andrey'

text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. " \
       "Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."

l = text.replace('.', '').split()
l.sort(key=len, reverse=True)
maxlen = 0
for i in l:
    if len(i) >= maxlen:
        maxlen = len(i)
        print i + "  Length = " + str(len(i))
