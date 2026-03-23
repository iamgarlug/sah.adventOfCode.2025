"""
Advent of Code 2025 — Day 1, Part 1
https://adventofcode.com/2025/day/1
"""

import math
from aoc.utils import parse

def solve(data: str):
    values = parse(data)

    position = 50
    zeroCount = 0

    for value in values:
        # Process input
        direction = 1 if value[:1] == "R" else -1
        distance = int(value[1:])

        # # The brute force way.
        # for i in range(distance):
        #     position += direction
        #     if position == -1:
        #         position = 99
        #     elif position == 100:
        #         position = 0
        # if position == 0:
        #     zeroCount += 1

        # There's probably a faster way to use a byte array with a mask to handle overflows.

        # Rotate the dial
        distance = (distance % 100) * direction # Modulus ignores multiple spins
        position += distance

        # Adjust position for overflows.
        if position > 99:
            position -= 100
        elif position < 0:
            position += 100

        if position == 0:
            zeroCount += 1

    return zeroCount
