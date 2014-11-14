def task4(array):
    if len(array) % 2 == 0:
        for element in array:
            if element % 2 != 0:
                array.remove(element)
    else:
        for element in array:
            if element % 2 == 0:
                array.remove(element)
    return array

print task4([1, 2, 3, 4])
print task4([1, 2, 3, 4, 5])