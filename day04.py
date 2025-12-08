from lib.grid import Point, Rect, DIRS

def parse(input: str) -> set[Point]:
    input = input.strip().split("\n")
    rolls: set[Point] = set()
    for j, row in enumerate(input):
        for i, s in enumerate(row):
            if s == '@':
                rolls.add(Point(i, j))
    return rolls

def accessible(rolls: set[Point]):
    for p in rolls:
        s = sum([1 if p + o in rolls else 0 for o in DIRS])
        if s < 4:
            yield p

def part1(input: str) -> int:
    """Solve part 1."""
    rolls = parse(input)
    return len(list(accessible(rolls)))

def part2(input: str) -> int:
    """Solve part 2."""
    rolls = parse(input)

    removed = 0
    while True:
        to_remove = set()
        for p in accessible(rolls):
            to_remove.add(p)
        if len(to_remove) == 0:
            break
        removed += len(to_remove)
        rolls = rolls - to_remove
            
    return removed


if __name__ == "__main__":
    from lib.runner import run_day
    run_day(4, part1, part2)
