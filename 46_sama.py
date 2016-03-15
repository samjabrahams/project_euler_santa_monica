from primerator.primerator import prime_generator as best_prime_generator_ever
import math

p = best_prime_generator_ever()

# Get primes under 10000
primes = []
for n in p:
    primes.append(n)
    if n > 10000:
        break

# Get odds under 10000
odds = []
i = 1
while i < 10000:
    odds.append(i)
    i += 2

# make list of squares * 2 up to 10000
squares = [2 * x * x for x in xrange(100)]

# Remove primes
odds = [x for x in odds if x not in primes]


for n in odds:
    a = True
    for p in primes:
        if n - p < 1:
            break
        if (n - p) in squares:
            a = False
    if a == True:
        print n
