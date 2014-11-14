__author__ = 'm_shalamov'


def even_odd_list(source_list):
    if len(source_list) % 2 == 0:
        for list_item in source_list:
            if list_item % 2 == 1:
                source_list.remove(list_item)
        return source_list
    else:
        for list_item in source_list:
            if list_item % 2 == 0:
                source_list.remove(list_item)
        return source_list


if __name__ == '__main__':
    print even_odd_list([1, 13, 12])
    print even_odd_list([1, 4, 13, 12])