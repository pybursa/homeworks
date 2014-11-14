a = ["a", 5, 2, 5, (1, "a"), "a"]
c = ["a", 5, 2, 5, (1, "a"), "a"]
b = []

for x in set(a):
    if a.count(x) > 1:
        a.remove(x)
print "assert unique_ordered: ", a

for x in c:
    if x not in c:
        c.append(x)

print "assert unique_disordered: ", c
