#!/usr/bin/python3
"""
A module to detrmine the winner of prime game
"""


def isPrime(num):
    """
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    A function to get the winner of the prime game
    """
    def count_primes(n):
        """
        A function to count prime numbers
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2

        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return sum(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        total_primes = count_primes(n)
        if total_primes % 2 == 0 or (total_primes == 1 and n != 1):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
