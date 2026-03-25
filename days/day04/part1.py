"""
Advent of Code 2025 — Day 4, Part 1
https://adventofcode.com/2025/day/4
"""

from aoc.utils import parse

def solve(data: str):
    lines = parse(data)
    rolls = 0

    emptyLine = '.' * len(lines[0])
    
    for lineNumber in range(0, len(lines)):
        previousLine = lines[lineNumber - 1] if lineNumber > 0 else emptyLine
        currentLine  = lines[lineNumber]
        nextLine     = lines[lineNumber + 1] if lineNumber < len(lines) - 1 else emptyLine
        rolls += countRollsInLine(previousLine, currentLine, nextLine)
    return rolls

def countRollsInLine(previousLine: str, currentLine: str, nextLine: str):
    rolls = 0

    for index in range(0, len(currentLine)):
        if currentLine[index] == '.':
            continue

        if isRollPickable(previousLine, currentLine, nextLine, index):
            rolls += 1

    return rolls

def isRollPickable(previousLine: str, currentLine: str, nextLine: str, index: int):
    # y increases downward
    positionsToCheck = [ [-1, -1], [ 0, -1], [ 1, -1],
                         [-1,  0],           [ 1,  0],
                         [-1,  1], [ 0,  1], [ 1,  1] ]

    neighboringRolls = 0

    for positionToCheck in positionsToCheck:
        x = positionToCheck[0] + index
        if (x < 0 or x >= len(currentLine)):
            continue
        y = positionToCheck[1]

        line = previousLine if y == -1 else currentLine if y == 0 else nextLine
        neighboringRolls += 1 if line[x] == '@' else 0

    return neighboringRolls < 4
