st = raw_input("Enter the string: ")
flag = True
i = 0

st = st.lower()
while i <= (len(st) / 2) and flag == True:
    if st[i] == st[len(st)-i-1]:
    	flag = True
    else:
    	flag = False
    i += 1

if flag == False:
 	print "No palindrome for you"
if flag == True:
	print "This string is a palindrome"
