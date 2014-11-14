__author__ = 'm_shalamov'

s = "wowhatamanwowowpalehche"

reference = 'wow'

result = 0

if len(reference) < len(s):
    for i in range(0, len(s)):
        if i+len(reference) < len(s):
            temp = s[i:i+len(reference)]
            if temp == reference:
                result += 1
else:
    print "Not able to find count"

print result