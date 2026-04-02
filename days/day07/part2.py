"""
Advent of Code 2025 — Day 6, Part 1
https://adventofcode.com/2025/day/6
"""

from aoc.utils import parse

def solve(data: str):
    lines = parse(data)
    lineLength = len(lines[0])
    beams = list() # The list of spaces with at least one path. This helps not having to scan the entire line.
    beamPathCount = [0] * lineLength # This will hold total number of tachyon paths.

    # Find starting beam.
    for index in range(0, lineLength):
        if lines[0][index] == 'S':
            beams.append(index)
            beamPathCount[index] += 1
            break

    for index in range(1, len(lines)):
        newBeams = list()
        for beamPointer in beams:
            line = lines[index]
            if isOpenSpace(line[beamPointer]):
                newBeams.append(beamPointer)
                # Do not change path count because the beam did not split.
            elif isSplitter(line[beamPointer]):
                # Split left.
                if beamPointer > 0:
                    newBeams.append(beamPointer-1)
                    beamPathCount[beamPointer-1] += beamPathCount[beamPointer]
                # Split right.
                if beamPointer < lineLength:
                    newBeams.append(beamPointer+1)
                    beamPathCount[beamPointer+1] += beamPathCount[beamPointer]
                # Reset since the beam split.
                beamPathCount[beamPointer] = 0 

        # Get rid of duplicates.
        beams = list(set(newBeams))
        # Sort since we need to scan left to right.
        beams.sort()
    return sum(beamPathCount)

def isBeam(c: chr):
    return c == '|'

def isOpenSpace(c: chr):
    return c == '.'

def isSplitter(c: chr):
    return c == '^'