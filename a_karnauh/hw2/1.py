def task1(array):
    if type(array) is tuple:
        return tuple(map(lambda a: a*a, array))
    else:
        return map(lambda a: a*a, array)
print task1((1, 2, 3))
print task1([1, 2, 3])