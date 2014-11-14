from collections import Counter
d = {1: 'j', 'u': 7.4, (5,7): [3, 1], "ii": 8}
i = 0
s = []
while i < len(d):
    s.append(type(d.keys()[i]).__name__) 
    s.append(type(d.values()[i]).__name__)
    i += 1
print Counter(s)


