s = "sabrrtuwacaddabra"
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print "text is: ", s
Q_last = s[0]
Comb = s[0]
maxlength = Comb
print "first one: ", Comb, ord(Comb)
for item in s:
#    print item, ord(item)
    if ord(item) < ord(Q_last):
        Comb = item
    else:
        Comb = Comb + item
#        print "current:",  Comb
    Q_last = item
    if len(Comb) > len(maxlength):
        maxlength = Comb
print ""
print "alphabetical text is: ", maxlength
