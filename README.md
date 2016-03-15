Let's solve some math!

Primerator
==========

This is a python module you can use to generate primes. Or more specifically, the first 50 million primes:

    >>> from primerator.primerator import prime_generator
    >>> p = prime_generator()
    >>> for prime in p:
    ...   # do things with primes
