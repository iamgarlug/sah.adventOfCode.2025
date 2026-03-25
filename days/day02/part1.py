"""
Advent of Code 2025 — Day 2, Part 1
https://adventofcode.com/2025/day/2
"""

from aoc.utils import parse

def solve(data: str):
    # Data is a single line. Split into an array.
    values = parse(data)[0].split(',')
    result = 0

    for value in values:
        minMax = value.split('-')
        # Add one because max is inclusive
        for i in range(int(minMax[0]), int(minMax[1]) + 1):
            numStr = str(i)
            length = len(numStr)

            # If the number is odd it cannot contain duplicate numbers
            if length % 2 == 1:
                continue

            # Get the substring numbers.
            halfLength = int(length / 2)
            left = numStr[0:halfLength]
            right = numStr[halfLength:]

            if left == right:
                result += i
    return result
