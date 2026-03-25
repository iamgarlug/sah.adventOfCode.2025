"""
Advent of Code 2025 — Day 1, Part 1
https://adventofcode.com/2025/day/1
"""

from aoc.utils import parse

def solve(data: str):
    values = parse(data)
    result = 0

    for numbers in values:
        leftIndex = 0
        leftDigit = 0
        rightIndex = 1
        rightDigit = 0
        currentIndex = 0

        for currentIndex in range(0, len(numbers)):
            currentDigit = int(numbers[currentIndex])

            if  currentDigit > leftDigit and currentIndex < len(numbers) - 1:
                leftIndex = currentIndex
                leftDigit = int(numbers[leftIndex])
                rightIndex = currentIndex + 1
                rightDigit = int(numbers[rightIndex])
            elif currentDigit > rightDigit:
                rightIndex = currentIndex
                rightDigit = int(numbers[rightIndex])

            # 99 is the max. We can skip the rest of the numbers.
            if leftDigit == 9 and rightDigit == 9:
                break

            currentIndex += 1

        result += leftDigit * 10 + rightDigit

    return result
