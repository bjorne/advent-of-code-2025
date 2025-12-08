from lib.range import overlaps, merge_overlapping

def parse(input: str) -> (list[range], list[int]):
    fresh, available = input.strip().split("\n\n")
    fresh = [
        range(int(s[0]), int(s[1])+1)
        for r in fresh.split("\n")
        if (s := r.split("-"))
    ]
    available = [int(n) for n in available.split("\n")]
    return fresh, available

def part1(input: str) -> int:
    """Solve part 1."""
    fresh, available = parse(input)

    def in_any_range(x: int, ranges: list[range]) -> bool:
        for r in ranges:
            if x in r:
                return True
        return False


    return len([f for f in available if in_any_range(f, fresh)])

def part2(input: str) -> int:
    """Solve part 2."""
    fresh, available = parse(input)

    return sum([len(range) for range in merge_overlapping(fresh)])
        

if __name__ == "__main__":
    from lib.runner import run_day
    run_day(5, part1, part2)
