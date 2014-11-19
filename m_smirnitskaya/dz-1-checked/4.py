s = raw_input("Enter your string: ")
l = []
lf = []
f = ''
s = s.lower()

for i in range(0,len(s)):
	j = i + 1

	while j <= len(s):
		l = list(s[i:j])
		t = ''.join(l)
		if t.isalpha():
			l.sort()
			if t == ''.join(l):
				f = t
		j += 1

	if len(f) == len(s) and len(f) != 1:
		lf.append(f)
		break
	elif f != "":
		lf.append(f)

if lf <> []:
    print "Longest:"
    for j in lf:
	    if len(j) == max(len(i) for i in lf):
	    	print j
	    	if len(j) == 1:
	    		print "You have just one character in your string"


'''
1) не забываем использовать 4 пробела вместо табуляции

ok!
[10/10]

'''
