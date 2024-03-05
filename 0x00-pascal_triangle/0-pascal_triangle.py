#!/usr/bin/python3
"""
Operation of pascal's triangle
"""


def pascal_triangle(n):
    """
        pascal triangle function taking
        Args:
            n - number of rows
    """
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n + 1):
        test = []
        if i == 1:
            pass
        else:
            for j in range(0, i):
                if j == 0 or j == i - 1:
                    test.append(1)
                else:
                    test.append(test2[j] + test2[j-1])
            test2 = test
            pascal.append(test)
    return pascal
