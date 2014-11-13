# coding=utf-8
def task08(string):
    """
    Задание 8: A-a-a (бонусное)

    УСЛОВИЕ:
    Посчитать в тексте количество букв "a" при условии что она окружена согласными
    ("car") и она не является первой или последней буквой слова.

    Текст:
    Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed,
    convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
    Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi,
    pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Sed porttitor lectus nibh.

    Согласные: все, кроме A, E, I, O, U, Y
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    amount = 0
    for word in string.split():
        for number, letter in enumerate(word):
            try:
                if word[number] == 'a' and word[number - 1] not in vowels and word[number + 1] not in vowels:
                    amount += 1
            except IndexError:
                pass
    return amount


if __name__ == '__main__':
    text = "Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, " \
           "convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices " \
           "posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. " \
           "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, " \
           "consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
           "Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, " \
           "elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh."
    print task08(text)

