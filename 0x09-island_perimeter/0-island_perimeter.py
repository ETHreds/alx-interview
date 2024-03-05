#!/usr/bin/python3
"""
Module to determine an island's perimeter
"""


def island_perimeter(grid):
    """
    A function to determine an
    island's perimeter
    """
    if not grid or not any(grid):
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
