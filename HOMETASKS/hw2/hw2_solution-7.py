# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 7: Сепаратор.Адвансед (бонусное)

УСЛОВИЕ:
Выполнить задание 5 ("Сепаратор") с дополнительным условием:
чтобы входящий список и список возвращаемый были одним и тем же объектом, т.е.
должна произойти модификация списка, а не пересборка нового.

start_list = [1,4,8,6,3,7,1]
end_list = [1,1,3,7,8,6,4]
(start_list is end_list) == True

Пример:
[1,4,8,6,3,7,1] is [1,1,3,7,8,6,4]
"""


def separ_inplace_1(L):
    M = L
    evens = []
    for item in L:
        if item % 2 == 0:
            evens.append(item)
            L.remove(item)
    L.sort()
    evens.sort(reverse=True)
    L.extend(evens)
    print M is L
    return L


if __name__ == "__main__":
    assert separ_inplace_1([1, 4, 8, 6, 3, 7, 1]) == [1, 1, 3, 7, 8, 6, 4]
