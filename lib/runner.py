import time
from pathlib import Path
from typing import Callable


def run_day(day: int, part1_fn: Callable[[str], int], part2_fn: Callable[[str], int]):
    """Run both parts of a day's puzzle with timing.

    Args:
        day: The day number (e.g., 1, 2, 3)
        part1_fn: Function that solves part 1
        part2_fn: Function that solves part 2
    """
    input_file = Path(f"day{day:02d}.txt")

    with open(input_file) as f:
        data = f.read()

    # Part 1
    start = time.perf_counter()
    result1 = part1_fn(data)
    elapsed1 = time.perf_counter() - start
    print(f"Part 1 ({elapsed1*1000:.3f}ms):")
    print(result1)

    # Part 2
    start = time.perf_counter()
    result2 = part2_fn(data)
    elapsed2 = time.perf_counter() - start
    print(f"Part 2 ({elapsed2*1000:.3f}ms):")
    print(result2)
