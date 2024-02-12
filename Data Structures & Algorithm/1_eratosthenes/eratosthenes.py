# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
# ​‌​‌‌​​​‌​‌​​​‌ Implement the sieve_of_eratosthenes function here below
def sieve_of_eratosthenes(n):
    """ Return the number of prime numbers between the range (2, n) """
    if n < 2:
        return 0

    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    p = 2

    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    z = 0
    for y in range(n + 1):
        if is_prime[y]:
            z += 1

    return z


# ​‌​‌‌​​​‌​‌​​​‌ Driver program
def main():
    n = -51
    nof_primes = sieve_of_eratosthenes(n)
    print("The number of primes between the range (2, {:d}) is: {:d}"
          .format(n, nof_primes))


if __name__ == "__main__":
    main()
