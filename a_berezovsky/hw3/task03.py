# coding=utf-8
def task03(string):
    """
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
    for sentence in string.split("."):
        words = []
        for word in sentence.split(" "):
            words.append(word[::-1])
        sentences.append(" ".join(words[::-1]))
    return ".".join(sentences[::-1])


if __name__ == '__main__':
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. " \
           "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. " \
           "Cras ultricies ligula sed magna dictum porta."
    print task03(text)

