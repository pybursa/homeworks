while True:
    n = raw_input("Enter any number: ")
    if n.isdigit():
    	break
    print "Please, enter a natural number."
l = []

for i in n:
	for k in range(0, int(i)):
		l.append('')

print "The sum of its digits is: ", len(l)



