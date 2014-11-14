a = 'abcdefghijklmnopqrstuvwxyz'
s = raw_input('Enter any string to find it the longest alphabetical series \n:')
e = ''
y = []
w = 0
for i in s:
    t=1
    d = w
    r = a.find(i)
    w = w + 1
    while s[d:d + t] == a[r:r + t]:
        f = s[d:d + t]
        t = t + 1
        if len(f) >= len(e):
            if len(f) > len(e):
                y = []
                y.append(f)
            if len(f) == len(e):
                y.append(f)
            e = f

if y == []:
    raw_input(' sorry, there are none')
else:
    print y
    raw_input('ready!')



