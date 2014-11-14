# -*- coding: cp1251 -*-
"""Задание 5: Сепаратор.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и модифицирует его следующим образом:
- в начале списка идут нечетные числа в порядке возрастания,
- далее идут четные числа в порядке убывания.
Пример:
[1,4,8,6,3,7,1] >> [1,1,3,7,8,6,4]"""


IN = [1,4,8,6,3,7,1]


def even(y):
    if y % 2 == 0:
        return True
    else:
        return False

def odd(y):
    if y % 2 != 0:
        return True
    else:
        return False



head = filter(odd, IN)
head.sort ()
tail = filter(even, IN)
tail.sort ()
tail.reverse ()
print head + tail





