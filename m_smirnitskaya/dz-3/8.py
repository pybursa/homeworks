st = "Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, \
lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum \
primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit \
neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum \
dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, \
consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur \
adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit \
nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, \
consectetur adipiscing elit. Sed porttitor lectus nibh."

#st = "cAr anna car, ca. a, hyai"
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
zn = [' ', '.', ',']
count = 0
st = st.lower()
print st

for i in range(len(st)):
	if (st[i] == 'a'): 
		if (st[i-1] and st[i+1]) not in zn:
			if (st[i+1] and st[i-1]) not in zn:
			    if (st[i-1] and st[i+1]) not in vowels:
			    	if st[i+1] and st[i-1] not in vowels:
				        print st[i-1:i+2]
				        count += 1
print "a: ", count
