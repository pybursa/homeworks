# -*- coding: cp1251 -*-

# Задание 10: интерактивный подсчет гласных.
# УСЛОВИЕ:
# Написать программу (python script), которая при запуске будет
# запрашивать пользователя ввести произвольную строку и
# выдавать в ответе количество гласных букв.
# Примечание:
# - для ручного ввода используем встроенную функцию raw_input();
# - для простоты на вход принимаем строку из букв латинского алфавита;
# - набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
# - программа должна быть нечувствительна к регистру.
# ВХОД: строка (ручной ввод пользователем)
# ВЫХОД: строка вида:
# "The string contains 2 vowels" - если гласные присутствуют,
# "The string doesn't contain vowels" - в противном случае.
# Пример:
# python ivowels.py - запуск
# Вывод:
# "Please, enter your string: "
# "wHAt Do yOU wANt fRom ME?"
# "The string contains 7 vowels"
# "Continue? (yes/no) "
# "maybe"
# "Please, enter corrent answer. Continue? (yes/no) "
# "yes"
# "Hurray!"
# "Please, enter your string: "
# "HHHMMMMM..."
# "The string doesn't contain vowels"
# "Continue? (yes/no) "
# "no"
# "It was nice to count your #vowels!"
# =========================================================================


print "==== Task 10: interactive vowels counting   ===="


check_str = "aeiou"

def vowels_count(arg):
    res = 0
    low_case_str = input_str.lower()
    for ch in low_case_str:
        if ch in check_str:
            res +=  1
    return res

y = "yes"
n = "no"

answer = y
while True:
    if answer == None:     
        answer = raw_input()
    
        if answer == n:
            print "Bye-Bye!"
            break
    
        if answer <> y:
            print "Please, enter corrent answer. Continue? (yes/no) "
            answer = None
            continue
            
        print "Hurray! :-)"
             
    print "Please, enter your string: "
    input_str = raw_input()
    res = vowels_count(input_str);
    if bool(res):
        print "The string contains", res, "vowels"
    else:
        print "The string doesn't contain vowels"
        
    answer = None
    print "Continue? (yes/no) "    
    
    

raw_input() 
    
    
    

       
    







        
            
            













