# -*- coding: cp1251 -*-

# Задание 2: подсчет гласных.
# УСЛОВИЕ:
# подсчет гласных букв в строке.
# Примечание:
# - для простоты на вход принимаем строку из букв латинского алфавита;
# - набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
# - программа должна быть нечувствительна к регистру.
# Пример:
# s = "hApPyHalLOweEn!"
# ...
# print result
# > 5
# =========================================================================


print "==== Task 2: Counting Vowels  ===="

input_str = "hApPyHalLOweEn!"
print 'INPUT: ', input_str


check_str = "aeiou"

# variant #1 =====================
entry_amount = 0
low_case_str = input_str.lower()
for ch in low_case_str:
    if ch in check_str:
        entry_amount +=  1
print "variant #1: ", entry_amount, "(For loop)"



# variant #2 =====================
low_case_str = input_str.lower()
l = [ch for ch in low_case_str if ch in check_str]
entry_amount = len(l)
print "variant #2: ", entry_amount, "(List generator)"

raw_input()
        
            
            













