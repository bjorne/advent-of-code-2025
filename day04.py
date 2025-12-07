from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

ORIGIN = Point(0, 0)
UP = Point(0, 1)
DOWN = Point(0, -1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
DIRS = [
    UP + LEFT,
    UP,
    UP + RIGHT,
    RIGHT,
    DOWN + RIGHT,
    DOWN,
    DOWN + LEFT,
    LEFT
]
            

@dataclass(frozen=True)
class Rect:
    a: Point
    b: Point

    def contains(self, p: Point) -> bool:
        a = self.a
        b = self.b
        return min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(a.y, b.y)

def parse(input: str) -> (Rect, set[Point]):
    input = input.strip().split("\n")
    w = len(input[0])
    h = len(input)
    rect = Rect(Point(0, 0), Point(w-1, h-1))
    print(rect)

    rolls: set[Point] = set()
    for j, row in enumerate(input):
        for i, s in enumerate(row):
            if s == '@':
                rolls.add(Point(i, j))
    return rect, rolls

def part1(input: str) -> int:
    """Solve part 1."""
    rect, rolls = parse(input)

    count = 0
    for p in rolls:
        s = sum([1 if p + o in rolls else 0 for o in DIRS])
        if s < 4:
            count += 1 
        
    return count


def part2(input: str) -> int:
    """Solve part 2."""
    rect, rolls = parse(input)

    removed = 0
    while True:
        to_remove = []
        for p in rolls:
            s = sum([1 if p + o in rolls else 0 for o in DIRS])
            if s < 4:
                to_remove.append(p)
        if len(to_remove) == 0:
            break
        removed += len(to_remove)
        rolls = rolls - set(to_remove)
            
    return removed


if __name__ == "__main__":
    with open("day04.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
