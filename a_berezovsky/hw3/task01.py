# coding=utf-8
def task01(string):
    """
    Задание 1: И снова гласные.

    УСЛОВИЕ:
    Посчитать количество гласных в каждом слове текста.
    Вывести максимальное количество гласных в одном слове.

    Текст:
    Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus.
    Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.

    Гласные: A, E, I, O, U, Y
    """

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    max_vowels = 0
    for word in string.split():
        vowels_in_word = 0
        for letter in word:
            if letter in vowels:
                vowels_in_word += 1
        if vowels_in_word > max_vowels:
            max_vowels = vowels_in_word
    return max_vowels

    # return max(map(
    # lambda word: reduce(lambda count, letter: count + 1 if letter in ['a', 'e', 'i', 'o', 'u', 'y'] else count,
    # word, 0), string.split()))


if __name__ == '__main__':
    text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. ' \
           'Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'
    print task01(text)

