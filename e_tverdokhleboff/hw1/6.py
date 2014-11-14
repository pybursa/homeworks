a = raw_input('Enter first value: ')
b = raw_input('Enter second value: ')

if type(a) is not int:
	print 'There is string typed'
elif type(b) is not int:
    print 'There is string typed'
elif a > b:
    print 'First value is greater than second'
elif a < b:
    print 'Second value is greater than firs'
elif a == b:
    print 'variables are equal'