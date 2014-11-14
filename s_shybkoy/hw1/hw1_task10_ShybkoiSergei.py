#hw 1/ task10/ Sergei Shybkoi

ans = 'yes'
while True:
    if ans == 'no':
        break
    print "Please enter your string:"
    s = raw_input().lower()
    if len(s) != 0:
        vowel = ['a', 'e', 'i', 'o', 'u']
        res = 0
        for ch in vowel:
            res += s.count(ch)
        print "There is(are)s " + str(res) + " vowel(s) in your string."
    else:
        print "You did not enter the string."
    print "Continue? (yes/no)"
    ans = raw_input().lower()
    if ans in ['yes', 'no']:
        continue
    else:
        while ans not in ['yes', 'no']:
            print "Please, enter correct answer. Continue? (yes/no) "
            ans = raw_input().lower()
