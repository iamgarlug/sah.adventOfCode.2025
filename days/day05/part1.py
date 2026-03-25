"""
Advent of Code 2025 — Day 5, Part 1
https://adventofcode.com/2025/day/5
"""

from aoc.utils import parse

def solve(data: str):
    lines = parse(data)
    freshCheckerDelegates = getFreshCheckerDelegatesFrom(lines)

    numberOfFreshIngredients = 0
    ingredientStartingIndex = len(freshCheckerDelegates) + 1 # delegates + 1 empty line
    for index in range(ingredientStartingIndex, len(lines)):
        ingredient = int(lines[index])
        for delegateItem in freshCheckerDelegates:
            delegate = delegateItem[0]
            leftBound = delegateItem[1]
            rightBound = delegateItem[2]
            isIngredientFresh = delegate(leftBound, rightBound, ingredient)
            if isIngredientFresh:
                numberOfFreshIngredients += 1
                break
    return numberOfFreshIngredients

def getFreshCheckerDelegatesFrom(lines: list[str]):
    delegates = list()

    index = 0
    while True:
        line = lines[index]
        if (line == ""):
            break

        bounds = line.split('-')
        delegates.append([ checkIdRange, int(bounds[0]), int(bounds[1]) ])

        index += 1
    return delegates

def checkIdRange(leftBound: int, rightBound: int, id: int):
    return leftBound <= id and id <= rightBound