a = "dth"
print "A = ", a
at = str(type(a))[7:-2]
print "type:", at

b = 5
print "B = ", b
bt = str(type(b))[7:-2]
print "type:", bt

if at == "str" or bt == "str":
	print "We have a string"
elif at == "int" and bt == "int":
	if a == b:
		print "A is equal to B"
	elif a > b:
		print "A is greater than B"
	elif b > a:
		print "B is greater than A"


'''
1) не забываем использовать 4 пробела вместо табуляции

ok!
[10/10]

'''
