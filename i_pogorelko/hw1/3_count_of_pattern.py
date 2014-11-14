s = "awowhatamanwowowpalehche"
p = "wow"
marker = "1"
wow_number  = 0
while s:
    if p in s:
        if marker=="0":
            s=s[1:]
#        print s
        if p in s[0:3]:
            print p
            wow_number +=1
        marker = "0"
    else:
        print "number of wow is: ", wow_number
        break
else:
    exit
