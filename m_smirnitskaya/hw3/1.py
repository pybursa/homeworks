st = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis\
 quis ac lectus. Donec rutrum congue leo eget malesuada."

l = st.split(' ')
l_number = []
n = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for i in l:
    for k in range(0, len(i)):
    	if i[k] in vowels:
    		n += 1
    l_number.append(n)
    n = 0
print "Input: ", st
print "Maximum number of vowels: ", max(l_number)

