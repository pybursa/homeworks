# coding=utf-8
"""
Задание 6: Классификатор. (бонусное)
УСЛОВИЕ:
Фрагмент кода, который принимает словарь со значениями элементов разных типов,
а возвращает словарь вида {имя_типа : количество_элементов_этого_типа}.
Пример:
{'a': 1, 3: [1,5], 'e': 'abc', '6': []} >> {'str': 1, 'list': 2, 'int': 1}
"""


def task06(input_data):
    return_data = {}
    for element in input_data.values():
        try:
            return_data[type(element).__name__] += 1
        except KeyError:
            return_data[type(element).__name__] = 1
    return return_data


if __name__ == '__main__':
    print task06({'a': 1, 3: [1, 5], 'e': 'abc', '6': []})

