# -*- coding: cp1251 -*-

# Задание 8: каждый третий.
# УСЛОВИЕ:
# Реализовать функционал который принимает кортеж
# и возвращает прореженный кортеж, оставляя только
# каждый третий элемент.
# Реализовать задачу двумя разными вариантами.
# Пример:
# t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
# ...
# > (3,6,9,'b')
# =========================================================================


print "==== Task 7: Unique Set  ===="

input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
print 'INPUT:', input_tuple


# variant #1
l = list(input_tuple)
res_1 = tuple(l[2::3])
print "Variant #1: ", res_1

# variant #2
res_2 = []
for x in range(len(input_tuple)):
    t = x+1
    if t % 3 == 0:
        res_2.append(input_tuple[x])
res_2 = tuple(res_2)
print "Variant #2: ", res_2

raw_input()



        
            
            













