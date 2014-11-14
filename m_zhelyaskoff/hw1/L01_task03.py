# -*- coding: cp1251 -*-

# Задание 3: подстчет вхождений подстроки.
# УСЛОВИЕ:
# Реализовать подсчеы количества вхождений подстроки "wow" в строке.
# ВХОД: строка
# ВЫХОД: число вхождений подстроки "wow"
# Пример:
# s = "wowhatamanwowowpalehche"
# ...
# > 3
# =========================================================================


print "==== Task 3: count entries of the substring ====="
input_str = "wowhatamanwowowpalehche"
sub_str = "wow"
print "INPUT:"
print "String: " + input_str
print "SubString: " + sub_str


print "OUTPUT: "
# variant #1
entry_amount = input_str.count(sub_str)
print "variant #1: ", entry_amount, "  (See the code !)"

# В примере задачи указано 3 вхождения.-Мне кажется это спорный
# вопрос поэтому 2 варината решения c разными результатами

# variant #2
entry_amount = 0
for s in range(len(input_str)):
    check_str = input_str[s:s+3]
    if check_str == sub_str:
        entry_amount += 1        
print "variant #2: ", entry_amount, "  (See the code !)"
        
raw_input()            
            













