def strange_func(arr):
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: x % 2 != 0
    if is_even(len(arr)):
        new_arr = filter(is_even, arr)
    else:
        new_arr = filter(is_odd, arr)
    return new_arr

print strange_func([3,7,12]) # >> [3,7]
print strange_func([3,7,12,7]) # >> [12]