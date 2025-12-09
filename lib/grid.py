from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
from itertools import pairwise

from .util import minmax

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def to(self, other: Point) -> Generator[Point]:
        x_step = -1 if other.x < self.x else 1
        y_step = -1 if other.y < self.y else 1
        for x in range(self.x, other.x + x_step, x_step):
            for y in range(self.y, other.y + y_step, y_step):
                yield Point(x, y)

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

    def area(self):
        a, b = self.a, self.b
        return abs(a.x - b.x + 1) * abs(a.y - b.y + 1)

    def corners(self):
        a, b = self.a, self.b
        return [
            a,
            a + Point(0, b.y - a.y),
            b,
            a + Point(b.x - a.x, 0)
        ]

def draw_points(points: list[Point], symbol: str = 'x', nosymbol: str = '.', pad: int = 0):
    min_x, max_x = minmax(map(lambda p: p.x, points))
    min_y, max_y = minmax(map(lambda p: p.y, points))

    for y in range(min_y - pad, max_y + 1 + pad):
        line = ''
        for x in range(min_x - pad, max_x + 1 + pad):
            if Point(x, y) in points:
                line += symbol
            else:
                line += nosymbol
        print(line)

def closed_walk(points: list[Point]) -> Generator[Point]:
    for a, b in pairwise(points + [points[0]]):
        for p in a.to(b):
            yield p
