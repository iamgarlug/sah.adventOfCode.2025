"""
Advent of Code 2025 — Day 5, Part 2
https://adventofcode.com/2025/day/5
"""

from aoc.utils import parse

# The tuple containing the left and right bounds.
class Range:
    def __init__(self, leftBound: int, rightBound: int):
        self.LeftBound = leftBound
        self.RightBound = rightBound

# A bi-directional linked list node
class Node:
    def __init__(self, range):
        self.Range = range
        self.Next = None

    def insertNode(self, previousNode: Node, newNode: Node):
        # New node is to the left of the current.
        if newNode.Range.LeftBound < self.Range.LeftBound:
            # Current node is first in linked list
            if previousNode is not None:
                previousNode.Next = newNode
            # Current node to the right of the new node.
            newNode.Next = self
        # End of linked list.
        elif self.Next is None:
            self.Next = newNode
        # Continue traversing the linked list.
        else:
            self.Next.insertNode(self, newNode)

    def collapseOverlappingNodes(self):
        if self.Next is None:
            return

        # No overlap. Continue.
        if self.Range.RightBound < self.Next.Range.LeftBound:
            self.Next.collapseOverlappingNodes()
            return

        # True overlap. Combine and continue.
        if self.Range.RightBound < self.Next.Range.RightBound:
            self.Range.RightBound = self.Next.Range.RightBound

        # Otherwise, the next node is completely contained and can be simply removed.

        self.Next = self.Next.Next
        self.collapseOverlappingNodes()

    def countIngredients(self):
        result = 0

        if self.Next is not None:
            result += self.Next.countIngredients()

        return result

# Boxing the linked list because Python does not pass by reference but allows modification of passed internals
class LinkedList:
    def __init__(self):
        self.Head = None

    def insertRanges(self, ranges: list[Range]):
        # Inserting a 0-0 range node guarantees it will always be the first node.
        self.Head = Node(Range(0, 0))

        for range in ranges:
            self.Head.insertNode(None, Node(range))

        return self

    def insertNode(self, newNode: Node):
        if self.Head is None:
            self.Head = newNode
        else:
            self.Head.insertNode(newNode)

    def collapseOverlappingNodes(self):
        self.Head.collapseOverlappingNodes()

    def countIngredients(self):
        # Skip the special head node.
        return self.Head.Next.countIngredients()

def getRanges(lines: list[str]):
    ranges = list()
    for line in lines:
        if line == "":
            break
        bounds = line.split('-')
        ranges.append(Range(int(bounds[0]), int(bounds[1])))
    return ranges

def solve(data: str):
    # Format ranges as objects
    ranges = getRanges(parse(data))

    linkedList = LinkedList().insertRanges(ranges)
    linkedList.collapseOverlappingNodes()
    numberOfIngredients = linkedList.countIngredients()
    return numberOfIngredients
