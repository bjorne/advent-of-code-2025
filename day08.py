from operator import itemgetter
from pprint import pp
import operator
from functools import reduce
from itertools import combinations

from lib.grid_3d import Point

def connect(input: str, num: int) -> int:
    junctions = set()
    for line in input.strip().split("\n"):
        x, y, z = map(int, line.split(","))
        junctions.add(Point(x, y, z))

    connections = set()
    dist = dict()
    for x, y in combinations(junctions, 2):
        dist[(x,y)] = x.euclidian_dist(y)

    connections = list(map(itemgetter(0), sorted(dist.items(), key=lambda x: x[1])[:num]))
    # connections.add(tuple(sorted((closest[0], closest[1]))))

    def expand_circuit(circuit: list[Point], p: Point) -> list[Point]:
        for c in connections:
            next = None
            if c[0] == p:
                next = c[1]
            if c[1] == p:
                next = c[0]
            if next:
                if next not in circuit:
                    circuit.append(next)
                    list(set(circuit)).sort()
                    circuit = sorted(list(set(circuit + expand_circuit(circuit, next))))

        return circuit

    circuits = set()
    for p in junctions:
        circuits.add(tuple(expand_circuit([p], p)))
    return reduce(operator.mul, sorted(map(len, circuits))[-3:])


def part1(input: str, num=1000) -> int:
    """Solve part 1."""
    return connect(input, num)


def part2(input: str, num=1000) -> int:
    """Solve part 2."""
    junctions = set()
    for line in input.strip().split("\n"):
        x, y, z = map(int, line.split(","))
        junctions.add(Point(x, y, z))

    dist = dict()
    for x, y in combinations(junctions, 2):
        dist[(x,y)] = x.euclidian_dist(y)

    sorted_dist = sorted(dist.items(), key=lambda x: x[1])
    connections = list(map(itemgetter(0), sorted_dist[:num]))
    # connections.add(tuple(sorted((closest[0], closest[1]))))

    def expand_circuit(circuit: list[Point], p: Point) -> list[Point]:
        for c in connections:
            next = None
            if c[0] == p:
                next = c[1]
            if c[1] == p:
                next = c[0]
            if next:
                if next not in circuit:
                    circuit.append(next)
                    list(set(circuit)).sort()
                    circuit = sorted(list(set(circuit + expand_circuit(circuit, next))))

        return circuit

    def compute_circuits():
        circuits = set()
        for p in junctions:
            circuits.add(tuple(expand_circuit([p], p)))
        return circuits

    circuits = compute_circuits()

    for i in range(num, len(sorted_dist)):
        pair = sorted_dist[i][0]
        connections.append(pair)
        a = set([circuit for circuit in circuits if pair[0] in circuit])
        b = set([circuit for circuit in circuits if pair[1] in circuit])

        if not a and not b:
            circuits.add(sorted([a, b]))
        else:
            # circuits where only a exist
            for circuit in a - b:
                circuits.add(pair[1]) # add b

            # circuits where only b exist
            for circuit in (b - a):
                circuits.add(pair[0]) # add a

            # circuits that can be linked
            for ca, cb in combinations((b | a) - (b & a), 2):
                if ca in a and cb in b:
                    print(a)
                    circuits.remove(a)
                    circuits.remove(b)
                    circuits.add(a | b)

        if len(compute_circuits()) <= 1:
            break
        # connections.append(

    return pair[0].x * pair[1].x



if __name__ == "__main__":
    with open("day08.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
