# coding=utf-8
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
[1,4,8,6,3,7,1] is [1,1,3,7,8,6,4
"""


def task07(input_data):
    data = input_data[:]
    del input_data[:]
    for element in sorted(data, reverse=True):
        if element % 2 == 0:
            input_data.append(element)
        else:
            input_data.insert(0, element)
    return input_data


if __name__ == '__main__':
    start_list = [1, 4, 8, 6, 3, 7, 1]
    print task07(start_list)
    print task07(start_list) == start_list

