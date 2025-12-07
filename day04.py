from lib.grid import Point, Rect, DIRS

def parse(input: str) -> set[Point]:
    input = input.strip().split("\n")
    rolls: set[Point] = set()
    for j, row in enumerate(input):
        for i, s in enumerate(row):
            if s == '@':
                rolls.add(Point(i, j))
    return rolls

def part1(input: str) -> int:
    """Solve part 1."""
    rolls = parse(input)

    count = 0
    for p in rolls:
        s = sum([1 if p + o in rolls else 0 for o in DIRS])
        if s < 4:
            count += 1 
        
    return count


def part2(input: str) -> int:
    """Solve part 2."""
    rolls = parse(input)

    removed = 0
    while True:
        to_remove = set()
        for p in rolls:
            s = sum([1 if p + o in rolls else 0 for o in DIRS])
            if s < 4:
                to_remove.add(p)
        if len(to_remove) == 0:
            break
        removed += len(to_remove)
        rolls = rolls - to_remove
            
    return removed


if __name__ == "__main__":
    with open("day04.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
