# -*- coding: utf-8 -*-
"""
Задание 10: интерактивный подсчет гласных.

УСЛОВИЕ:
Написать программу (python script), которая при запуске будет запрашивать пользователя ввести произвольную строку и
выдавать в ответе количество гласных букв.
Примечание:
- для ручного ввода используем встроенную функцию raw_input();
- для простоты на вход принимаем строку из букв латинского алфавита;
- набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
- программа должна быть нечувствительна к регистру.

ВХОД: строка (ручной ввод пользователем)
ВЫХОД: строка вида:
"The string contains 2 vowels" - если гласные присутствуют,
"The string doesn't contain vowels" - в противном случае.

Пример:
python ivowels.py - запуск

Вывод:
"Please, enter your string: "
"wHAt Do yOU wANt fRom ME?"
"The string contains 7 vowels"
"Continue? (yes/no) "
"maybe"
"Please, enter corrent answer. Continue? (yes/no) "
"yes"
"Hurray!"
"Please, enter your string: "
"HHHMMMMM..."
"The string doesn't contain vowels"
"Continue? (yes/no) "
"no"
"It was nice to count your vowels!"
"""
import task02


def process_vowels(string):
    vowels = task02.task2(string)
    if vowels > 0:
        print "The string contains %d vowels" % vowels
    else:
        print "The string doesn't contain vowels"


def process_choices():
    prompt = ""
    while prompt != "yes" and prompt != "no":
        prompt = raw_input("Continue? (yes/no) ")
        if prompt == "no":
            print "It was nice to count your vowels!"
            return False
        elif prompt == "yes":
            return True
        else:
            print "Please, enter corrent answer."


if __name__ == '__main__':
    process_vowels(raw_input("Please, enter your string: "))
    while process_choices():
        process_vowels(raw_input("Please, enter your string: "))
