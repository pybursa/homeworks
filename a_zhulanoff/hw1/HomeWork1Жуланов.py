# revers 1
a = 'ambulance'
result = a [::-1]
print result

# revers 2



# revers 3
# revers 4

# countChars
def countChars(chars, text):
    i = 0
    for char in text:
        if char in chars or char in chars.upper():
            i += 1
    return i

text = "hApPyHaLOweEn"
count = countChars("", text)

print (count)

# countWow
a = 'wowhatamanwowowpalehche'
sub = 'wow'
print(a.count(sub))