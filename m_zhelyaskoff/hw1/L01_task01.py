# -*- coding: cp1251 -*-

# Задание 1: реверс строки.
# УСЛОВИЕ:
# Преобразовать строку "ecnalubma" в
# ее зеркальное отражение (реверсировать).
# Сделать это четырьмя разными способами.
# ВХОД: строка
# ВЫХОД: реверсированная строка
# Пример:
# a = "ambulance"
# ...
# print result
# > "ecnalubma"

print "==== Task 1: Reverse a String  ===="
input_str = "ecnalubma"
print 'INPUT: ', input_str

# variant #1 ==============================
result = input_str[::-1] 
print "Variant #1: ", result

# variant #2 ==============================
l = list(input_str)
res = []
for x in range(len(l)):   
    res.insert(0, l[x:x+1][0])
result = "".join(res)
print "Variant #2: ", result

# variant #3 ===============================
res = list(input_str)
res.reverse()
result = "".join(res)
print "Variant #3: ", result

# variant #4 ===============================
result = ''
for i in input_str:
    result = i + result
print "Variant #4: ", result

raw_input()
