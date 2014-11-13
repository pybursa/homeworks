
st = 'ecnalubma'
print "Input: ", st

# 1
print "Output #1 (using [::-1]): ", st[::-1]

st2 = ''
# 2
for i in reversed(range(0,len(st))):
	st2 += st[i]
print "Output #2 (using for loop): ", st2

# 3
l = list(st)
for i in range(0,len(l)):
    l[i] = ord(l[i])

l.reverse()
for i in range(0,len(l)):
	l[i] = chr(l[i])
print "Output #3 (using ord and chr): ",''.join(l)

    
# 4
l = list(st)
for i in range(0,len(l)/2):
	l[i], l[-i-1] = l[-i-1], l[i]
print "Output #4 (another for loop): ", ''.join(l)


'''
1) не забываем использовать 4 пробела вместо табуляции

ok!
[10/10]

'''
