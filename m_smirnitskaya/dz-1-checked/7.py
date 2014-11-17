l = [5, 5, 7, 3, 6, 7, 8, 3, 5, 8, 4, 11, 678]
print "Input: ", l
s = list(l)
s.sort()
t = []

for i in range(0, len(l)):
	if s[i-1] <> s[i]:
		t.append(s[i])
print "Output (sorted): ", t
t = []

for i in range(0, len(l)):
	n = 0
	for j in range(0,i):
		if l[i] == l[j]:
			n += 1
	if n == 0:
		t.append(l[i])
print "Output (unsorted): ", t


'''
1) подразумевалась не сортировка списка, а сохранение порядка следования элементов в первичном списке,
в итоге реализация unsorted это то, что требовалось от sorted
2) и не забываем использовать 4 пробела вместо табуляции

ok!
[7/10]

'''
