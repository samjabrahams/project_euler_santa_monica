import subprocess
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def prime_generator():
    for x in range(1, 51):
        with open(os.path.join(BASE_DIR, 'primes' + str(x) + '.txt')) as inf:
            tokens = inf.read().split()
            for token in tokens:
                try:
                    i = int(token)
                    yield i
                except Exception as e:
                    print e
                    print 'Not a number:', token


def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
