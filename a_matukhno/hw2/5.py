# -*- coding: utf-8 -*-
"""
Задание 5: Сепаратор.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и модифицирует его следующим образом:
- в начале списка идут нечетные числа в порядке возрастания,
- далее идут четные числа в порядке убывания.
Пример:
[1,4,8,6,3,7,1] >> [1,1,3,7,8,6,4]
"""

s = [1, 4, 8, 6, 3, 7, 1]


def task5(x):
    odd = []  # нечетное
    even = []  # четное

    for el in x:
        if el % 2 != 0 or el == 1:
            odd.append(el)
        elif el % 2 == 0:
            even.append(el)
        else:
            print "Incorrect element"
    odd.sort()
    even.sort(reverse=True)
    return odd + even


if __name__ == '__main__':
    print task5(s)