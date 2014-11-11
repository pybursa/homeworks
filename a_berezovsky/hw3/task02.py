# coding=utf-8
from string import punctuation, maketrans


def task02(string):
    """
    Задание 2: Самое длинное слово.

    УСЛОВИЕ:
    Найти слово максимальной длины в тексте.
    Вывести это слово. Если таких слов несколько - вывести все.

    Текст:
    Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus.
    Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
    """
    string = string.translate(maketrans("", ""), punctuation)
    words = [""]
    for word in string.split():
        if len(word) > len(words[0]):
            words = [word]
        elif len(word) == len(words[0]):
            words.append(word)
    return " ".join(words)


if __name__ == '__main__':
    text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. " \
           "Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
    print task02(text)

