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
