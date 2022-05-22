import math

def is_prime_number(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

for i in range(1, 1000001):
    if is_prime_number(i):
        print(i, end=' ')