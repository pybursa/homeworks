s = "hApPyHalLOweEn!"
l  = s.lower()
vocal_num = 0
for i in l:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#        print i
        vocal_num +=1

print "sum of vowel letters is: ", vocal_num
