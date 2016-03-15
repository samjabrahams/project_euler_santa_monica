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
