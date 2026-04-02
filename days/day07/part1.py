"""
Advent of Code 2025 — Day 6, Part 1
https://adventofcode.com/2025/day/6
"""

from aoc.utils import parse

# Appears from the test input that a splitter with splitters to the immediate left and right does not count towards splitting.


def solve(data: str):
    lines = parse(data)
    beams = list()
    timesSplit = 0

    # Find starting beam
    for index in range(0, len(lines[0])):
        if lines[0][index] == 'S':
            beams.append(index)
            break

    for index in range(1, len(lines)):
        newBeams = list()
        for beamPointer in beams:
            if isOpenSpace(lines[index][beamPointer]):
                newBeams.append(beamPointer)
            elif isSplitter(lines[index][beamPointer]):
                newBeams.append(beamPointer-1)
                newBeams.append(beamPointer+1)
                timesSplit += 1
        beams = list(set(newBeams)) # Get rid of duplicates.
    return timesSplit

def isBeam(c: chr):
    return c == '|'

def isOpenSpace(c: chr):
    return c == '.'

def isSplitter(c: chr):
    return c == '^'