
import random
rep = ''
while rep != "t" and rep != "l" and rep != "r":
    rep = raw_input("Enter 't' for tuple and 'l' for a list (or 'r' for random choice): ")
if rep == "r":
    rep = random.choice(["t", "l"])
if rep == "t":
	print "Your choice is tuple"
elif rep == "l":
    print "Your choice is list"
ls = []
l = ''

l = raw_input("Enter the list of numbers separated with a space: ")
ls = l.split(' ')
try:

    for i, k in enumerate(ls):
	    ls[i] = int(k)**2

    if rep == "t":
	    ls = tuple(ls)

    print ls
except:
	print "Oops, something went wrong. Please, try to be more careful next time."