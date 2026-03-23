"""
Advent of Code 2025 — Day 1, Part 2
https://adventofcode.com/2025/day/1
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
            numStrLen = len(numStr)

            compareLen = int(numStrLen/2)

            while True:
                if compareLen < 1:
                    # Minimum reached. Exit loop
                    break

                # Only check if the string can be equally divided into substrings.
                if (numStrLen % compareLen == 0):
                    substringNumbers = [numStr[i:i+compareLen] for i in range(0, numStrLen, compareLen)]
                    first = substringNumbers[0]
                    if all(x == first for x in substringNumbers):
                        result += i
                        break

                # Decrement and continue
                compareLen -= 1
    return result
