#hw 1/ task2/ Sergei Shybkoi

print "Enter string:"
s = raw_input().lower()
if len(s) != 0:
    vowel = ['a', 'e', 'i', 'o', 'u']
    res = 0
    for ch in vowel:
        res += s.count(ch)
    print "There is(are)s " + str(res) + " vowel(s) in your string."
else:
    print "You did not enter the string. Try to restart app."


