def t(n):
	if isinstance(n, int):
		return "int"
	elif isinstance(n, str):
		return "str"
	elif isinstance(n,list):
		return "list"
	elif isinstance(n,dict):
		return "dict"
	elif isinstance(n,tuple):
		return "tuple"
	elif isinstance(n,type):
		return "function"
        else:
            return "something else"

a = 6
print a, " - ", t(a)
b = "hgr"
print b, " - ", t(b)
c = [5, 7, "tydth"]
print c, " - ", t(c)
d = (5, 3, 2, 2, 667)
print d, " - ", t(d)
e = {1: "one", 2: "two", 3: "three"}
print e, " - ", t(e)
f = int
print f, " - ", t(f)


'''
1) не забываем использовать 4 пробела вместо табуляции

ok!
[10/10]

'''
