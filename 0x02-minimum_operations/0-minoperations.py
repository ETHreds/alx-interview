#!/usr/bin/python3
"""
No MODs to be imported
"""


def minOperations(n):
    """
    A function that returns the min number of
    operations needed
    """
    op = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            n //= factor
            op += factor
        else:
            factor += 1
    return op
