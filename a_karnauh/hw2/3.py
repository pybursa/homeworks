def task3(array):
    d = {}
    for element in array:
        d[element] = element%3 == 0
    return d

print task3([1, 2, 3])