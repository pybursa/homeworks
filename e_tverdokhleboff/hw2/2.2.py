word = str(raw_input("Enter your word:\n"))
f = len(word)
s = len(word) / 2
if len(word) % 2 != 0:
    print 'False'
elif word[-1:s+1] == word[s-1:f:-1]:
    print 'True'
else:
    print 'False'