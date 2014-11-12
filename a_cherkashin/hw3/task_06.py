def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


for i in xrange(2,10000):
    if is_prime(i):
        print i
