import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from aoc.runner import run


def main():
    args = sys.argv[1:]

    if len(args) < 2 or len(args) > 3:
        print("Usage: py aoc <day> <part> [test]")
        print("  Example: py aoc 8 1")
        print("  Example: py aoc 8 1 test")
        sys.exit(1)

    try:
        day = int(args[0])
        part = int(args[1])
    except ValueError:
        print("Error: <day> and <part> must be integers.")
        sys.exit(1)

    if part not in (1, 2):
        print("Error: <part> must be 1 or 2.")
        sys.exit(1)

    test = False
    if len(args) == 3:
        if args[2] != "test":
            print(f"Error: unrecognized argument '{args[2]}'. Did you mean 'test'?")
            sys.exit(1)
        test = True

    run(day, part, test=test)


main()
