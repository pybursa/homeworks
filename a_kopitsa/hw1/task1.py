# -*- coding: utf-8 -*-
mystring = "ambulance"
print "Реверс строки ->  " + mystring
print "====================================="

print "SPOSOB 1"
print "Результат ->  " + ''.join(reversed(mystring))
print "====================================="

print "SPOSOB 2"
print "Результат ->  " + mystring[::-1]
print "====================================="

print "SPOSOB 3"
mystringls = list(mystring)
mystringls.reverse()
print "Результат ->  " + ''.join(mystringls)

print "====================================="
print "SPOSOB 4"
stroka = ""
for letter in mystring[::-1]:
    stroka += letter
print "Результат ->  " + stroka

print "====================================="
print "SPOSOB 5"
dlina = len(mystring)
newstring = ""
ls = list(mystring)
for x in range(dlina+1):
    if x != 0:
        newstring += mystring[-x]
print "Результат ->  " + newstring

print "====================================="
print "SPOSOB 6"
dlina = len(mystring)
count = 0
newstring = ""
while (count < dlina) :
    count = count + 1
    newstring += mystring[-count]
print "Результат ->  " + newstring

print "====================================="
print "SPOSOB 7"
newstring = ""
dlina = len(mystring)
while(dlina >= 1):
    newstring += mystring[dlina-1]
    dlina -= 1
print "Результат ->  " + newstring
