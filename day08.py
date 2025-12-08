from operator import itemgetter
from pprint import pp
import operator
from functools import reduce
from itertools import combinations, islice, dropwhile
from typing import Generator

from lib.grid_3d import Point

def connect_circuits(input: str) -> Generator[tuple[tuple[Point, Point], set[frozenset[Point]]]]:
    junctions = set()
    for line in input.strip().split("\n"):
        x, y, z = map(int, line.split(","))
        junctions.add(Point(x, y, z))
    dist: dict[tuple[Point, Point], float] = dict()
    for x, y in combinations(junctions, 2):
        dist[(x,y)] = x.euclidian_dist(y)
    sorted_dist = sorted(dist.items(), key=lambda x: x[1])

    circuits: set[frozenset[Point]] = set((frozenset([j]) for j in junctions))
    for (a, b), _ in sorted_dist:
        ac = next((circuit for circuit in circuits if a in circuit))
        bc = next((circuit for circuit in circuits if b in circuit))
        if ac != bc:
            # join two circuits
            circuits.remove(ac)
            circuits.remove(bc)
            circuits.add(ac | bc)

        yield ((a, b), circuits)


def part1(input: str, num=1000) -> int:
    """Solve part 1."""
    last = next(islice(connect_circuits(input), num-1, num))
    return reduce(operator.mul, sorted([len(c) for c in last[1]], reverse=True)[0:3])


def part2(input: str) -> int:
    """Solve part 2."""
    last = next(islice(dropwhile(lambda tup: tup[0] < 10 or len(tup[1][1]) > 1, enumerate(connect_circuits(input))), 1), [])
    (a, b), _ = last[1]
    return a.x * b.x


if __name__ == "__main__":
    from lib.runner import run_day
    run_day(8, part1, part2)
