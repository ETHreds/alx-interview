#!/usr/bin/python3
"""
No modules to be imported at this time
"""


def makeChange(coins, total):
    """
    A function to determine total number of coins neede to make
    the total value
    Args:
        coins: List containing int values
        total: total value to be met
    """
    dp = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
