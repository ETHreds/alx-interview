#!/usr/bin/python3
"""minOperations whatever the function do"""


def minOperations(n):
    """ Whatever the function does"""
    if not isinstance(n, int) or n <= 1 :
        return 0

    def find_divisors(number):
        """Documentation"""
        divisors = []
        for divisor in range(2, number + 1):
            while number % divisor == 0:
                divisors.append(divisor)
                number //= divisor
        return divisors

    prime_divisors = find_divisors(n)
    operations = 0
    clipboard = 0

    for divisor in prime_divisors:
        if is_prime(divisor):
            clipboard += divisor
        else:
            operations += (clipboard // divisor)  # Copy-Paste
            clipboard %= divisor

    operations += clipboard  # Paste

    return operations


def is_prime(number):
    """Number is prime"""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
