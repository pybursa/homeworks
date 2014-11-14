vowels = ('a', 'e', 'i', 'o', 'u')
need_continue = 'yes'
while need_continue == 'yes':
    user_input = raw_input('Please, enter your string: ')
    length = len( re.findall('|'.join(vowels), user_input.lower()) )
    if length == 0:
        print "The string doesn't contain vowels"
    elif length == 1:
        print "The string contains 1 vowel"
    else:
        print "The string contains %s vowels" % length
    need_continue = raw_input("Continue? (yes/no) ")

