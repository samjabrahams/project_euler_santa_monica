from primerator.primerator import prime_generator
import math
import sys

def is_square(n):
    return int(math.sqrt(n))**2 == n

def is_solution(candidate, primes):
    for p in primes:
        if p > candidate:
            continue
        if is_square(0.5*(candidate - p)):
            return False
    return True

def solve_the_problem():
    g = prime_generator()
    known_primes = []
    candidate_number = 9
    for prime in g:
        known_primes.append(prime)
        while candidate_number < prime:
            if is_solution(candidate_number, known_primes):
                print "Solution:", candidate_number
                sys.exit(0)
            else:
                candidate_number += 2

solve_the_problem()
