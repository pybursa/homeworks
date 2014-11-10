#!/usr/bin/python
# -*- coding: utf-8 -*-


# Задание 10: интерактивный подсчет гласных.
def vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string:
        if letter.lower() in vowels:
            count += 1
    return count


def main():
    """ main function which does all stuff
    """
    prompt = "Please, enter your string: "
    vowels_message = "The string contains %d vowels"
    novowels_message = "The string doesn't contain vowels"
    more_question = "Continue? (yes/no) "
    warning = "Please, enter corrent answer. " + more_question
    yes_message = "Hurray!"
    no_message = "It was nice to count your vowels!"
    answer = None

    while True:
        if not answer:
            string = raw_input(prompt)
            vowels_count = vowels(string)
            if vowels_count > 0:
                print(vowels_message % vowels_count)
            else:
                print(novowels_message)

        answer = raw_input(warning if answer else more_question)
        if answer == "no":
            print(no_message)
            break
        elif answer == "yes":
            print(yes_message)
            answer = None
            continue


if __name__ == "__main__":
    assert vowels("hApPyHalLOweEn!") == 5
    main()
