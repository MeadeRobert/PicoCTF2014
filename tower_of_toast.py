import math
import functools

primes = []


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

i = 2
while len(primes) < 40:
    if(is_prime(i)):
        primes.append(i)
    i += 1

print(primes)

print(functools.reduce(lambda x, y: y * x, primes, 1))