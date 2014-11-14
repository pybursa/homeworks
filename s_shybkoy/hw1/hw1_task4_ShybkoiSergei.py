#hw 1/ task4/ Sergei Shybkoi

print "Enter string:"
s = raw_input()
if len(s) != 0:
    res = x = s[0]
    for i in range(1, len(s), 1):
        if s[i] >= s[i-1]:
            x += s[i]
        else:
            x = s[i]
        if len(x) > len(res):
            res = x
    print "Result: ", res
else:
    print "You did not enter the string. Try to restart app."