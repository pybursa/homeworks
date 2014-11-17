d1 = {65: 'tyg', 'y65': {5: 6, 7: 8}, (6, 7): ['hjk', 65, "hf"], 6: 78, (6, 4): {"jg": 765}}
ni = 0
ns = 0
nd = 0
nl = 0
nt = 0
print "Input: ", d1
for i in d1.keys():
 	if type(i).__name__ == "int":
 		ni += 1
 	elif type(i).__name__ == "str":
 		ns += 1
 	elif type(i).__name__ == "dict":
 		nd += 1
 	elif type(i).__name__ == "tuple":
 		nt += 1
 	elif type(i).__name__ == "list":
 		nl += 1

for i in d1.values():
 	if type(i).__name__ == "int":
 		ni += 1
 	elif type(i).__name__ == "str":
 		ns += 1
 	elif type(i).__name__ == "dict":
 		nd += 1
 	elif type(i).__name__ == "tuple":
 		nt += 1
 	elif type(i).__name__ == "list":
 		nl += 1
d2 = {}
d2['str'] = ns
d2['int'] = ni
d2['dict'] = nd
d2['tuple'] = nt
d2['list'] = nl
print "Output: ", d2