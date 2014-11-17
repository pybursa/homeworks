st = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis \
quis ac lectus. Donec rutrum congue leo eget malesuada."

l = st.split(' ')

l_length = []
for i in l:
	i = i.replace('.', '')
	l_length.append(len(i))
    
print "Input: ", st

print "Max: ", max(l_length)

for i in l:
	if len(i.replace('.', '')) == max(l_length):
		print i.replace('.', '')	
