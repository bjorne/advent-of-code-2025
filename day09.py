from itertools import combinations

from lib.grid import Point, Rect, draw_points, closed_walk
from lib.util import minmax

def parse(input:str) -> list[Point]:
    points = list()
    for line in input.strip().split("\n"):
        x, y = line.split(",")
        points.append(Point(int(x), int(y)))

    return points

def part1(input: str) -> int:
    """Solve part 1."""
    grid = set(parse(input))
    rect = max([Rect(a, b) for a, b in combinations(grid, 2)], key=lambda r: r.area())
    print(rect)
    return rect.area()


def part2(input: str) -> int:
    """Solve part 2."""
    points = parse(input)
    edge = set(closed_walk(points))
    points_set = set(points)
    print(f"edge is {len(edge)}")
    min_x, max_x = minmax(map(lambda p: p.x, points))
    min_y, max_y = minmax(map(lambda p: p.y, points))
    print("minmax done")
    # draw_points(edge, symbol='o', pad=2)
    print("drawn")
    max_area = 0
    for a, b in combinations(points, 2):
        if a.x == b.x or a.y == b.y:
            continue
        rect = Rect(a, b)
        rect_area = rect.area()
        if rect_area < max_area:
            continue
        corners_inside = 0
        for corner in rect.corners():
            if corner in points_set or corner in edge:
                corners_inside += 1
                continue
            # send a ray
            count = 0
            # draw_points(edge + rect.corners() + list(corner.to(Point(max_x + 10, corner.y))), pad=5)
            for p in corner.to(Point(max_x + 1, corner.y)):
                if p in edge:
                    count += 1
            if count == 1:
                corners_inside += 1
        if corners_inside == 4:
            max_area = max(max_area, rect_area)

    return max_area



if __name__ == "__main__":
    from lib.runner import run_day
    run_day(9, part1, part2)
