numprimes = 10000
count = 0
prime = 2


def firstprimes(prime):
    divisor = 2
    while divisor <= prime:
        if prime == 2:
            return True
        elif prime % divisor == 0:
            return False
            break
        while prime % divisor != 0:
            if prime - divisor > 1:
                divisor += 1
            else:
                return True

while count < int(numprimes):
    if firstprimes(prime) == True:
        print '#' + str(count + 1), '-', prime, ';' 
        count += 1
        prime += 1
    else:
        prime += 1

