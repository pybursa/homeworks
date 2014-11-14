#hw 1/ task3/ Sergei Shybkoi

print "Enter string:"
s = raw_input()
if len(s) != 0:
    ch = 'wow'
    s1 = s
    res = 0
    i = s1.find(ch)
    while i > -1:
        res += 1
        s1 = s1[i+1:len(s1)]
        i = s1.find(ch)
    print "There is(are)s " + str(res) + " 'wow' in your string."
else:
    print "You did not enter the string. Try to restart app."
