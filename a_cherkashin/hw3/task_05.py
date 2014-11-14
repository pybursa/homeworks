def pseudo_sum(number):
    total_digit = 0
    for digit in list(str(number)):
       total_digit -= int(digit)
    return abs(total_digit)

print pseudo_sum(456)
