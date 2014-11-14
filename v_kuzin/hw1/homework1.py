#!/usr/bin/env python
# -*- coding: utf-8 -*-
#task 1
a='ambulanse' #input all
print '*****************************************'
print 'INPUT=',a
n=len(a)  #length
print '========================================='
print 'method 1'
b=[]

for i in a:
    b.insert(0,i)

result=''.join(b)
print result

print '========================================='
print 'method 2'
d=[]

for i in a:
    d.extend(i)

d.reverse()
result1="".join(d)
print result1

print '========================================='
print 'method 3'
result2=''

for i in xrange(0,n):
    result2=d.pop()+result2

print result2

print '========================================='
print 'method 4'
result3=''

for i in xrange(0,n):
    result3=a[i]+result3

print result3
