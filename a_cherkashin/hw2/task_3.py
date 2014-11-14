def div_by_three(arr):
    by_three = {}
    for i in arr:
        by_three[i] = i % 3 == 0
    return by_three

print div_by_three([3,7,12])