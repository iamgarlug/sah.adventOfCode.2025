"""
Advent of Code 2025 — Day 6, Part 1
https://adventofcode.com/2025/day/6
"""

import math
from aoc.utils import parse

def solve(data: str):
    lines = parse(data)

    # Use a sliding window

    rightBound = len(lines[0])

    leftPointer = 0
    rightPointer = 0
    mathAnswer = 0

    while rightPointer <= rightBound:
        if not isThePointerAtAColumnEnd(rightPointer, lines):
            rightPointer += 1
            continue

        mathAnswer += calculateColumn(leftPointer, rightPointer, lines)
        rightPointer += 1
        leftPointer = rightPointer

    return mathAnswer

def isThePointerAtAColumnEnd(pointer: int, lines: list[str]):
    if (pointer == len(lines[0])):
        return True

    for line in lines:
        if line[pointer] != ' ':
            return False
    return True

def calculateColumn(leftPointer: int, rightPointer: int, lines: list[str]):
    numbers = list()

    for index in range(0, len(lines)-1):
        numberString = lines[index][leftPointer:rightPointer].strip()
        numbers.append(int(numberString))

    operator = lines[len(lines)-1][leftPointer:rightPointer].strip()
    if operator == "*":
        result = 1
        for number in numbers:
            result *= number
        return result
    else:
        result = 0
        for number in numbers:
            result += number
        return result