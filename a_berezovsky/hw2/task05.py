# coding=utf-8
"""
Задание 5: Сепаратор.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и модифицирует его следующим образом:
- в начале списка идут нечетные числа в порядке возрастания,
- далее идут четные числа в порядке убывания.
Пример:
[1,4,8,6,3,7,1] >> [1,1,3,7,8,6,4]
"""

def task05(input_data):
    # odd_array = []
    # even_array = []
    # for element in input_data:
    #     if element % 2 == 0:
    #         even_array.append(element)
    #     else:
    #         odd_array.append(element)
    return sorted(element for element in input_data if element % 2 == 1) + sorted(
        element for element in input_data if element % 2 == 0)[::-1]


if __name__ == '__main__':
    print task05([1, 4, 8, 6, 3, 7, 1])

