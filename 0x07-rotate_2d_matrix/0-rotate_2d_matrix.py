#!/usr/bin/python3
"""
No modules to be imported at this time
"""


def rotate_2d_matrix(matrix):
    """
    """
    matrix[:] = \
        [
        [matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
    for row in matrix:
        row.reverse()
