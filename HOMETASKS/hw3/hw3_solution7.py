#!/usr/bin/env python
# -*- coding: utf8 -*-

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
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta.
"""

__author__ = 'wowkalucky'


TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. \
Cras ultricies ligula sed magna dictum porta."""


import string


def simple_reverse_1(text):

    ends = ".!?"
    else_punctuation = filter(lambda s: s not in ends, string.punctuation)
    print "punctuation", else_punctuation
    print "ends", ends

    mem_dict = {}
    for symbol in text:
        if symbol in string.punctuation:
            print symbol
            mem_dict[symbol] = mem_dict.setdefault(symbol, 0) + 1
    print mem_dict

    sentenses = [sentense.strip() for sentense in text.split(".")]
    print "0", sentenses
    sentenses.reverse()
    print "1", sentenses
    worded_sentenses = []
    for sentense in sentenses:
        words = sentense.split()
        words.reverse()
        worded_sentenses.append(words)
    print "2", worded_sentenses
    result = []
    for sentense in worded_sentenses:
        for word in sentense:
            result.append(word[::-1])
    result = " ".join(result)
    return result


if __name__ == "__main__":
    test_text = """Abc, dfg!!! Klm, nopq. Rst, xyz?"""
    simple_reverse_1(test_text)
    # assert simple_reverse_1(test_text) == """zyx tsR qpon mlK gfd cbA"""
