from lib.grid import Point, LEFT, RIGHT, UP
from functools import cache

def parse(input: str) -> (list[str], set[Point], Point):
    lines = input.strip().split("\n")
    splitters: set[Point] = set()
    start = None
    for j, line in enumerate(lines):
        for i, s in enumerate(line):
            if line[i] == '^':
                splitters.add(Point(i, j))
            elif line[i] == 'S':
                start = Point(i, j)
    assert start is not None
    return lines, splitters, start

def part1(input: str) -> int:
    """Solve part 1."""
    lines, splitters, start = parse(input)
    beams = set([start.x])
    splits = 0
    for y in range(start.y + 1, len(lines)):
        new_beams = beams.copy()
        for beam in beams:
            if Point(beam, y) in splitters:
                splits += 1
                new_beams.remove(beam)
                new_beams.add(beam-1)
                new_beams.add(beam+1)
        beams = new_beams
    return splits

def part2(input: str) -> int:
    """Solve part 2."""
    lines, splitters, start = parse(input)
    beams = set([start.x])
    splits = 0

    @cache
    def timelines(beam: Point) -> int:
        if beam.y >= len(lines):
            return 1
        if beam in splitters:
            return timelines(beam + RIGHT + UP) + timelines(beam + LEFT + UP)
        return timelines(beam + UP)

    return timelines(start)


if __name__ == "__main__":
    with open("day07.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
