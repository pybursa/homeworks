# -*- coding: utf8 -*-
__author__ = 'wowkalucky'


"""
Задание 6: Классификатор. (бонусное)

УСЛОВИЕ:
Фрагмент кода, который принимает словарь со значениями элементов разных типов,
а возвращает словарь вида {имя_типа : количество_элементов_этого_типа}.

Пример:
{'a': 1, 3: [1,5], 'e': 'abc', '6': []} >> {'str': 1, 'list': 2, 'int': 1}
"""


def classified_1(D):
    result = {}
    for value in D.values():
        type_name = type(value).__name__
        if type_name in result:
            result[type_name] += 1
        else:
            result[type_name] = 1
    return result


def classified_2(D):
    result = {}
    for value in D.values():
        type_name = type(value).__name__
        result[type_name] = result.setdefault(type_name, 0) + 1
    return result


if __name__ == "__main__":
    print classified_1({'a': 1, 3: [1,5], 'e': 'abc', '6': []})
    print classified_2({'a': 1, 3: [1,5], 'e': 'abc', '6': []})
    assert classified_1({'a': 1, 3: [1,5], 'e': 'abc', '6': []}) == {'str': 1, 'list': 2, 'int': 1}
