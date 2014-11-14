c = True
while c:
    print 'Please, enter your string:'
    text = raw_input()
    r = text.lower().count('a') + text.lower().count('e') + text.lower().count('i') + text.lower().count('o') + text.lower().count('u') +   text.lower().count('y')
    if r > 0:
        print 'The string contains ' +  str(r) + ' vowels'
    else:
        print "The string doesn't contain vowels"
    a = ""
    while a!='yes':    
        print "Continue? (yes/no)"
        a = raw_input()
        if a == 'yes':
            c = True  
        elif a == 'no':
            c = False
            print "It was nice to count your vowels!"
            break
        else:
            print "Really? Try again"
            c = True
        
    
