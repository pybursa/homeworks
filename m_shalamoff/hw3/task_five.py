__author__ = 'm_shalamov'


def sum_natural_numbers(source_int):
    list_int = list(str(source_int))

    result = 0

    for list_item in list_int:
        result += int(list_item)

    print result


if __name__ == '__main__':
    sum_natural_numbers(123)