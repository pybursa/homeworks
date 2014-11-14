# sum 2 integers without using '+'
def bitSum(a, b):
    result = a ^ b
    carry = (a & b) << 1
    if carry != 0:
        return bitSum(result, carry)
    else:
        return result

# convert to string and back
def pseudosum(num):
    result = 0
    for char in str(num):
        result = bitSum(result, int(char))
    return result

print pseudosum(1234)