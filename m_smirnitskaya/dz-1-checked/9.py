x = raw_input("Enter x: ")
y = raw_input("Enter y: ")
z = raw_input("Enter z: ")
def switch(d):
	return { z: y, x: switch2(max(x, y))}.get(d, '')
def switch2(d):
	return {x: x, y: z}.get(d, '')

print switch(max(x, z))


'''
1) реализация некорректаная

ok!
[3/10]

'''
