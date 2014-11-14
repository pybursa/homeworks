def task5(array):
    even = []
    odd = []
    result = []
    for element in array:
        if element % 2 == 0:
            odd.append(element)
        else:
            even.append(element)
    even.sort()
    odd.sort(reverse=True)
    return even + odd
print task5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])