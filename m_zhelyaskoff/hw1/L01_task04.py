# -*- coding: cp1251 -*-

# Задание 4: упорядоченная подстрока.
# УСЛОВИЕ:
# Построить функционал который будет находить в строке
# подстроку максимальной длины, в которой буквы
# упорядочены в алфавитном порядке.
#
# ВХОД: строка
# ВЫХОД: подстрока
# Пример:
# s = "sabrrtuwacaddabra"
# ...
# > "abrrtuw"
# =========================================================================


print "==== Task 4: Orderly substring  ===="
input_str = "sabrrtuwacaddabra"
# input_str = "sacaddabraabrrtuw"  -  for test

print "INPUT:"
print "String: " + input_str


print "OUTPUT: "
low_case_list = list(input_str.lower())

string = ""
max_len_str = ""
char_code = 0

for ch in range(len(low_case_list)):  
    if char_code > ord(low_case_list[ch]):
        char_code = 0
        if len(string) > len(max_len_str):
            max_len_str = string
        string = ""
        
    char_code = ord(low_case_list[ch])       
    string += low_case_list[ch]
  
if len(string) > len(max_len_str):
    max_len_str = string
 
print "Result: ", max_len_str

raw_input()


        
            
            













