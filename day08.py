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
    a, b = None, None
    for i in range(num, len(sorted_dist)):
        a, b = sorted_dist[i][0]
        connections.append((a,b))
        ac = [circuit for circuit in circuits if a in circuit][0]
        bc = [circuit for circuit in circuits if b in circuit][0]
        if not ac and not bc:
            circuits.add(tuple(sorted((a, b))))
        elif ac and bc and ac == bc:
            continue
        elif ac and bc:
            circuits.remove(ac)
            circuits.remove(bc)
            circuits.add(tuple(sorted(ac + bc)))
            if len(circuits) <= 1:
                break
        elif ac:
            ac.add(b)
        elif bc:
            ac.add(a)
        else:
            raise Exception("unreachable")

    return a.x * b.x


if __name__ == "__main__":
    from lib.runner import run_day
    run_day(8, part1, part2)
