n = ''

def vocal(smth):
    vocals = ['a', 'e', 'i', 'o', 'u']
    n2 = smth.lower()
    s = 0
    print "Vowels:"
    for i in range(0,len(smth)):
	    if n2[i] in vocals:
		    print smth[i]
		    s += 1
    if s == 0:
    	print "The string does not contain any vowels"
    else:
    	print "Number of vowels:", s


def cont():
    rep = raw_input("Continue? (yes/no) ")
    if rep == "yes":
        beg()
    elif rep == "no":
        print "It was nice to count your vowels!"
    else:
    	print "Please, enter 'yes' or 'no'"
    	cont()

def beg():
    n = raw_input("Enter anything you want: ")
    vocal(n)
    cont()


beg()


'''
1) не забываем использовать 4 пробела вместо табуляции
2) вывод немного отличается от условия

ok!
[10/10]

'''
