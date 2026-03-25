import importlib.util
import traceback
from pathlib import Path

_PROJECT_ROOT = Path(__file__).parent.parent
_DAYS_DIR = _PROJECT_ROOT / "days"


def run(day: int, part: int, test_file: str | None = None) -> None:
    day_dir = _DAYS_DIR / f"day{day:02d}"

    if not day_dir.exists():
        print(f"Error: No solution found for day {day}.")
        print(f"  Create the folder: days/day{day:02d}/")
        return

    part_file = day_dir / f"part{part}.py"
    if not part_file.exists():
        print(f"Error: No part {part} solution found for day {day}.")
        print(f"  Create the file: days/day{day:02d}/part{part}.py")
        return

    input_filename = f"{test_file}.txt" if test_file else "input.txt"
    input_file = day_dir / input_filename
    if not input_file.exists():
        print(f"Error: Input file not found: days/day{day:02d}/{input_filename}")
        if test_file:
            print("  Create it and paste the sample input from the problem page.")
        else:
            print("  Create it and paste your puzzle input.")
        return

    raw_input = input_file.read_text(encoding="utf-8")

    spec = importlib.util.spec_from_file_location(f"day{day:02d}_part{part}", part_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    solve_fn = getattr(module, "solve", None)
    if solve_fn is None:
        print(f"Error: days/day{day:02d}/part{part}.py has no 'solve' function.")
        print("  Add 'def solve(data: str):' to the file.")
        return

    label = f"Day {day}, Part {part}"
    if test_file:
        label += f" [{test_file.upper()}]"
    print(label)
    print("-" * len(label))

    try:
        result = solve_fn(raw_input)
    except Exception as e:
        print(f"Error during execution: {type(e).__name__}: {e}")
        traceback.print_exc()
        return

    print(f"Answer: {result}")
