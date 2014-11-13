import os, sys

while True:
    rep = raw_input("What module are you interested in? (os or sys) ")
    if rep == "os" or rep == "sys":
    	break
    else:
    	print "Please, enter the name of the module"


print rep, ":"
if rep == "os":
    print dir(os)
if rep == "sys":
    print dir(sys)
rep2 = raw_input("Enter the name of the function to get help:")
rep2 = rep + '.' + rep2
print help(rep2)


