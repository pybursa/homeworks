#hw 1/ task1/ Sergei Shybkoi

s = 'ecnalubma'
print "Initial string: ", s
print "After reverse:"

res1 = s[-1::-1]
print res1

res2 = ''
for i in range(-1, -1*(len(s)+1), -1):
    res2 += s[i]
print res2

x = list(s)
x.reverse()
res3 = ''.join(x)
print res3

res4 = ''
for i in range(0,len(x)):
    res4 += x[i]
print res4



