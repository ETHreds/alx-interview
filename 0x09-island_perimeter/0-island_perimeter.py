#!/usr/bin/python3

# Calculates perimeter of a grid


def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                # cells horizontally adjacent
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
                # cells vertically adjacent
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter

