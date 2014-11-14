s = 'abnba'
c = True
i = 0
j = len (s) - 1
while (j - i) >=1:
    if s[i] == s[j]:
        c = True
    else:
        c = False
    i += 1
    j += - 1
print c
