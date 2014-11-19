# coding=utf-8
u"""
Task 02 PyBursa HW4

УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине (исключение первое слово),
и в конце нужно добавить троеточие ("...").

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.

Пример:
text = "Proin eget tortor risus."
limit = 24
output = "Proin eget tortor risus."
limit = 23
output = "Proin eget tortor..."
limit = 13
output = "Proin eget..."
limit = 6
output = "Pro..."
"""


def task02(text, length):
    """
    Shrinks text for fixed length
    :param text: input text
    :param length: maximum return length
    :return result_text: processed text
    """
    if len(text) <= length:
        return text
    splitted_text = text.split()
    if len(splitted_text[0]) >= length - 3:
        return splitted_text[0][:length - 3] + "..."
    result_text = []
    for word in splitted_text:
        if len(" ".join(result_text)) + len(word) >= length - len("..."):
            return " ".join(result_text) + "..."
        else:
            result_text.append(word)
    return result_text

