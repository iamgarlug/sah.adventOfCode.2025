# Advent of Code 2025

Python solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Requirements

Python 3.6+

> **Note:** On some Windows machines `py` maps to Python 2.7 (e.g. from windows-build-tools).
> If you hit a syntax error, use `py -3`, `python`, or `python3` instead.

## Usage

Run from the project root:

```
py aoc <day> <part>
py aoc <day> <part> test
```

| Command | Description |
|---|---|
| `py aoc 8 1` | Day 8, Part 1 — real puzzle input |
| `py aoc 8 2` | Day 8, Part 2 — real puzzle input |
| `py aoc 8 1 test` | Day 8, Part 1 — sample/test input |
| `py aoc 8 2 test` | Day 8, Part 2 — sample/test input |

## Adding a New Day

1. **Create the day folder**, e.g. for Day 8:
   ```
   days/day08/
   ```

2. **Add the input files:**
   - `days/day08/input.txt` — paste your puzzle input
   - `days/day08/test.txt` — paste the sample input from the problem page

3. **Add the solution files** using this template:

   `days/day08/part1.py`
   ```python
   def parse(data: str):
       return data.strip().splitlines()

   def solve(data: str):
       values = parse(data)
       # TODO: implement
       return None
   ```

   `days/day08/part2.py` — same structure with its own `solve(data: str)`.

4. **Run it:**
   ```
   py aoc 8 1 test   # verify against sample first
   py aoc 8 1        # then run against real input
   ```

The only contract each solution file must satisfy is defining a `solve(data: str)` function that accepts the raw input string and returns the answer.

## Project Structure

```
├── aoc/
│   ├── __main__.py   # CLI entry point
│   └── runner.py     # Loads day module and runs the solution
└── days/
    └── dayXX/
        ├── part1.py  # def solve(data: str)
        ├── part2.py  # def solve(data: str)
        ├── input.txt # Real puzzle input
        └── test.txt  # Sample input from problem page
```
