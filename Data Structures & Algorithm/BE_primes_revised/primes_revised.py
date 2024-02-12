# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
#​‌​‌‌​​​‌​‌​​​‌ Implement the nof_primes_revised function here below
import math


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def nof_primes_revised(list):
    """ Return the number of prime numbers in a list """
    count = 0
    primes = set()
    composites = set()
    for i in list:
        if i in primes:
            count = count + 1
        elif i in composites:
            pass
        else:
            if is_prime(i):
                primes.add(i)
                count = count + 1
            else:
                composites.add(i)
    return count

