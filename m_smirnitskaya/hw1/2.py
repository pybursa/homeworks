n = raw_input("Enter anything you want: ")
vocals = ['a', 'e', 'i', 'o', 'u']
n2 = n.lower()
s = 0
print "Vowels:"
for i in range(0,len(n)):
	if n2[i] in vocals:
		print n[i]
		s += 1
if s == 0:
	print "The string does not contain any vowels"
else:
    print "Number of vowels:", s


'''
1) не забываем использовать 4 пробела вместо табуляции

ok!
[10/10]

'''
