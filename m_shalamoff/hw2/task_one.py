__author__ = 'm_shalamov'


def list_tuple_involution(obj):
    result = []
    if type(obj) is list:
        for list_item in obj:
            result.append(pow(list_item, 2))
        return result
    elif type(obj) is tuple:
        for list_item in obj:
            result.append(pow(list_item, 2))
        return tuple(result)
    else:
        return "Unsupported object type"


if __name__ == '__main__':
    print list_tuple_involution([1, 2, 3])
    print list_tuple_involution((1, 2, 3))
    print list_tuple_involution('str')