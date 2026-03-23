"""
Advent of Code 2025 — Day 1, Part 2
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
        #     if position == 0:
        #         zeroCount += 1
        #     position += direction
        #     if position == -1:
        #         position = 99
        #     elif position == 100:
        #         position = 0

        # There's probably a faster way to use a byte array with a mask to handle overflows.

        # Count the number of "extra" spins.
        zeroCount += math.floor(distance / 100)

        # Don't count the last spin of a "perfect" rotation if we started at zero. The landing is counted separately.
        if position == 0 and distance >= 100 and distance % 100 == 0:
            zeroCount -= 1

        # Rotate the dial
        startedFromZero = position == 0 # If we start at zero then we cannot "cross" zero
        position += (distance % 100) * direction # Modulus ignores multiple spins

        if position < 0:
            zeroCount += 1 if not startedFromZero else 0
            position += 100
        elif position == 100:
            position = 0
        elif position > 100:
            zeroCount += 1
            position -= 100

        if position == 0:
            zeroCount += 1

    print(position)
    return zeroCount
