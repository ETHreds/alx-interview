#!/usr/bin/python3
"""
Calculate grid perimeter
"""


def island_perimeter(grid):
    """Takes grid and loop through rows and columns"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                """
                horizontal adjacent
                """
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
                """
                vertical adjacent
                """
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
    return perimeter
