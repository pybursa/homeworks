__author__ = 'alex'


def task_2():
    vowels = ('a', 'e', 'i', 'o', 'u')
    user_input = raw_input('Any your string: ')
    vow = sum(1 for t in user_input.lower() if t in vowels)

    print vow


task_2()