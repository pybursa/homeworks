st = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem\
 ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing\
  elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna \
  dictum porta."
print "------------INPUT--------------"
print st
l = st.split('.')

print "-----------OUTPUT-----------"
l.reverse()
l1 = l

l_d = []
l_final = []
st = ''
for i in l1:
	l_d = i.strip().split(' ')
	l_d.reverse()
	for j in range(len(l_d)):
		l_d[j] = l_d[j][::-1]
        	# fixing commas
		if l_d[j][0:1] == ',':
			l_d[j] = l_d[j][1:] + ','
	# fixing first letters
	l_d[-1] = l_d[-1].lower()
	l_d[0] = l_d[0].capitalize()

	s_t = st + ' '.join(l_d)
	l_final.append(s_t)

print '. '.join(l_final)[2:] + '.'

