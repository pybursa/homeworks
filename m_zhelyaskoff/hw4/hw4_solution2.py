#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
Задание 2: Послесловие...

УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в \
случае, если текст не помещается в ограничение обрезать его, но при этом слова \
не должны обрываться на середине (исключение первое слово), и в конце нужно \
добавить троеточие ("...").

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada.
"""


__author__ = "Mihail Zhelyaskov aka m_zhelyaskoff"
__copyright__ = "Copyright 2014, The Homework Project"
__version__ = "0.0.1"
__maintainer__ = "Mihail Zhelyaskov"
__email__ = "mzhelyaskov@yandex.ru"
__status__ = "Production"



TEXT = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum \
porta. Donec rutrum congue leo eget malesuada."""



def ellipsis_1(text, len_limit=0):
    u"""function(str, int) -> str

    Разбивает текст по словам, в конце добавляет троеточие так чтобы
    результирующая длина текста не привышала len_limit
    Если len_limit не передается или равен 0 текст возвращается целиком

    Описание аргументов:
    text -- входной текст
    len_limit -- максимальная длина выходного текста (default 0)
    """

    if len_limit == 0:
        return text

    limit = max(3, len_limit)
    text = text[:limit].strip()

    # if the last character is dot, ellipsis is't added
    if text[::-limit] == '.':
        return text

    l = text.rsplit(' ', 1)
    text = l[0]
    if len(text) > limit-3:
        l = text.rsplit(' ', 1)
        text = l[0]
    if len(l) == 1:
        text = l[0][:limit-3]
    text = text + "..."
    return text[:len_limit]




if __name__ == '__main__':
    assert cut_the_text("Proin eget tortor risus.", 24) == "Proin eget tortor risus."

    assert cut_the_text("Proin eget tortor risus.", 23) == "Proin eget tortor..."
    assert cut_the_text("Proin eget tortor risus.", 22) == "Proin eget tortor..."
    assert cut_the_text("Proin eget tortor risus.", 21) == "Proin eget tortor..."
    assert cut_the_text("Proin eget tortor risus.", 20) == "Proin eget tortor..."

    assert cut_the_text("Proin eget tortor risus.", 19) == "Proin eget..."
    assert cut_the_text("Proin eget tortor risus.", 18) == "Proin eget..."
    assert cut_the_text("Proin eget tortor risus.", 17) == "Proin eget..."
    assert cut_the_text("Proin eget tortor risus.", 16) == "Proin eget..."
    assert cut_the_text("Proin eget tortor risus.", 15) == "Proin eget..."
    assert cut_the_text("Proin eget tortor risus.", 14) == "Proin eget..."
    assert cut_the_text("Proin eget tortor risus.", 13) == "Proin eget..."

    assert cut_the_text("Proin eget tortor risus.", 12) == "Proin..."
    assert cut_the_text("Proin eget tortor risus.", 11) == "Proin..."
    assert cut_the_text("Proin eget tortor risus.", 10) == "Proin..."
    assert cut_the_text("Proin eget tortor risus.", 9)  == "Proin..."
    assert cut_the_text("Proin eget tortor risus.", 8)  == "Proin..."

    assert cut_the_text("Proin eget tortor risus.", 7)  == "Proi..."
    assert cut_the_text("Proin eget tortor risus.", 6)  == "Pro..."
    assert cut_the_text("Proin eget tortor risus.", 5)  == "Pr..."
    assert cut_the_text("Proin eget tortor risus.", 4)  == "P..."
    assert cut_the_text("Proin eget tortor risus.", 3)  == "..."
    assert cut_the_text("Proin eget tortor risus.", 2)  == ".."
    assert cut_the_text("Proin eget tortor risus.", 1)  == "."
    assert cut_the_text("Proin eget tortor risus.", 0)  == ""

    print "Ok"
