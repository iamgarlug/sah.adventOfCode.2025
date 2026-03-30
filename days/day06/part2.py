"""
Advent of Code 2025 — Day 6, Part 2
https://adventofcode.com/2025/day/6
"""

from aoc.utils import parse

def solve(data: str):
    lines = parse(data)

    # Still use a sliding window. Just need to move from right to left and read numbers vertically

    leftBound = -1
    rightBound = len(lines[0])

    leftPointer = rightBound - 1
    rightPointer = rightBound - 1

    mathAnswer = 0

    while leftPointer >= leftBound:
        if not isThePointerAtAColumnStart(leftPointer, lines):
            leftPointer -= 1
            continue

        mathAnswer += calculateColumn(leftPointer, rightPointer, lines)
        leftPointer -= 1
        rightPointer = leftPointer

    return mathAnswer

def isThePointerAtAColumnStart(pointer: int, lines: list[str]):
    if (pointer < 0):
        return True
    for line in lines:
        if line[pointer] != ' ':
            return False
    return True

# We can still move from left to right as * and + are commulative.
def calculateColumn(leftPointer: int, rightPointer: int, lines: list[str]):
    numbers = list()

    lastLine = lines[len(lines)-1]
    operator = lastLine[leftPointer+1] # Need to add 1 because the left pointer is currently on the column divider

    for index in range(rightPointer, leftPointer, -1):
        number = getNumberFromColumn(index, lines)
        numbers.append(number)

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

def getNumberFromColumn(pointer: int, lines:list[str]):
    numberString = ""
    for index in range(0, len(lines)-1):
        if lines[index][pointer] in ['*', '+']:
            break
        else:
            numberString += lines[index][pointer]
    return int(numberString.strip())
