"""
Advent of Code 2025 — Day 3, Part 2
https://adventofcode.com/2025/day/3
"""

from aoc.utils import parse

def solve(data: str):
    lines = parse(data)
    result = 0

    # Recursion might make this simpler.
    for numbers in lines:
        numStr = ""
        indexOfMaxDigit = -1
        for digitsLeft in range(12, 0, -1):
            indexOfMaxDigit = findIndexOfMaxValue(numbers, indexOfMaxDigit + 1, digitsLeft)
            numStr += numbers[indexOfMaxDigit]
        result += int(numStr)

    return result

def findIndexOfMaxValue(numbers: str, startIndex: int, digitsLeft: int):
    maxDigit = 0
    maxDigitIndex = 0

    stopIndexExclusive = len(numbers) - digitsLeft + 1
    for currentIndex in range(startIndex, stopIndexExclusive):
        currentDigit = int(numbers[currentIndex])

        if currentDigit > maxDigit:
            maxDigit = currentDigit
            maxDigitIndex = currentIndex
        
        # 9 is the largest possible value
        if maxDigit == 9:
            break

        currentIndex += 1
    
    return maxDigitIndex