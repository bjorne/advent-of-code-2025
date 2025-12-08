from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __lt__(self, other: Point) -> bool:
        return self.euclidian_dist(ORIGIN) < other.euclidian_dist(ORIGIN)

    def euclidian_dist(self, other: Point) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

ORIGIN = Point(0, 0, 0)
