__author__ = 'm_shalamov'


def list_separator(source_list):
    even_list = []
    odd_list = []
    for list_item in source_list:
        if list_item % 2 == 0:
            even_list.append(list_item)
        else:
            odd_list.append(list_item)
    return odd_list + even_list


if __name__ == '__main__':
    print list_separator([1, 2, 3, 4])
