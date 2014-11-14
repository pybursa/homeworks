# Author: Oleg Shestakov
# -*- coding: utf-8 -*-

# Задание 10: интерактивный подсчет гласных.
# УСЛОВИЕ:
# Написать программу (python script), которая при запуске будет
# запрашивать пользователя ввести произвольную строку и выдавать в ответе количество гласных букв.
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
# "It was nice to count your vowels!"


def switch_case(case):
    return {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True
    }.get(case, False)


def count_vowels(string):
    count = 0
    temp = string.lower()
    for i in temp:
        if switch_case(i):
            count += 1
    return count


def correct_answer(answer):
    if answer == "yes":
        print "Hurray!"
        vowels()
    elif answer == "no":
        print "It was nice to count your vowels!"
        return
    else:
        print "Please, enter corrent answer. Continue? (yes/no)"
        correct_answer(raw_input())
    return


def vowels():
    print "Please, enter your string: "
    string = raw_input()
    vowels_count = count_vowels(string)
    if vowels_count > 0:
        print "The string contains", vowels_count, "vowels"
    else:
        print "The string doesn't contain vowels"
    print "Continue?(yes/no)"
    answer = raw_input()
    correct_answer(answer)
    return


vowels()

