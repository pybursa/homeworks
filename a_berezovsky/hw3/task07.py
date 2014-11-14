# coding=utf-8
from string import punctuation


def move_punctuation(string):
    for symbol in punctuation:
        if symbol in string:
            string = string.split(" %s" % symbol)
            string = ("%s " % symbol).join(string)
    return string


def task07(string):
    """
    Задание 7: Реверс'em all! (бонусное)

    УСЛОВИЕ:
    Выполнить задание 3 с сохранением позиций:
    - знаков препинания ("word," >> "drow,");
    - Заглавных букв в начале предложения ("Word ..." >> "Drow ...").




    Задание 3: Реверс'em!

    УСЛОВИЕ:
    Изменить в тексте порядок следования:
    - букв в словах;
    - слов в предложениях;
    - предложений в тексте.
    Вывести модифицированный текст.

    Текст:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada.
    Cras ultricies ligula sed magna dictum porta.

    """
    sentences = []
    for sentence in string.split(".")[:-1]:
        words = []
        for word in sentence.strip().split(" "):
            words.append("".join(word[::-1]))
        sentence = (" ".join(words[::-1])).capitalize()
        sentences.append(move_punctuation(sentence))
    return ". ".join(sentences[::-1]) + "."


if __name__ == '__main__':
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. " \
           "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. " \
           "Cras ultricies ligula sed magna dictum porta."
    print task07(text)

