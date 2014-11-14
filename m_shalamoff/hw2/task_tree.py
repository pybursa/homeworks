__author__ = 'm_shalamov'


def generate_dict(source_list):
    result = {}
    for list_item in source_list:
        if list_item % 3 == 0:
            result.update({list_item: True})
        else:
            result.update({list_item: False})
    return result


if __name__ == '__main__':
    print generate_dict([1, 3, 4])