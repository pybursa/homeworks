def separator(arr):
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: x % 2 != 0

    evens = filter(is_even, arr)
    odds = filter(is_odd, arr)

    sorted_odds = sorted(odds)
    sorted_evens = sorted(evens, reverse=True)

    return sorted_odds + sorted_evens

print separator([1,1,3,7,8,6,4])