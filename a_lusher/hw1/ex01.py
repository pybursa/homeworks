#!usr/bin/python

#my_string=raw_input("Please enter a string: ")
my_string="Hello World!"

# Method N 1

reverse1=my_string[::-1]
print "Method 1"
print reverse1
print ""

# Method N 2

reverse2=''
for i in range(len(my_string)-1,-1,-1):
	reverse2+=my_string[i]
print "Method 2"
print reverse2
print ""

# Method N 3

reverse3=''
i=len(my_string)-1
while i>=0:
	reverse3+=my_string[i]
	i-=1
print "Method 3"
print reverse3
print ""

# Method N 4
my_list=list()
i=0
while i<len(my_string):
	my_list.append(my_string[i])
	i+=1
print "Method 4"
# Why is the following not working?!
print my_list.reverse()