#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 10
# ? - a,e,i,o,u
print '*****************************************'

for i in xrange(0,50):
    print "Please, enter your string: "
    s=raw_input()
    s1=s.lower()     # A-->a
    s2=s1.count('a')+s1.count('e')+s1.count('i')+s1.count('o')+s1.count('u')
    if s2==0:
        print "The string doesn't contain vowels"
    else:
        print 'The string contains ',s2,' vowels'

    print "Continue? (yes/no) "
    s=raw_input()
    s=s.lower()     # A-->a
    if s=='yes':
        continue
    elif s=='no':
        print "It was nice to count your vowels!"
        break
    else:
        print "Please, enter corrent answer. Continue? (yes/no) "
        s=raw_input()
        s=s.lower()     # A-->a
        if s=='yes':
            print "Hurray!"
            continue
        elif s=='no':
            print "It was nice to count your vowels!"
            break
        else:
            print "I'm tired, I'm broke ... wake me later"
            break
print '*****************************************'
