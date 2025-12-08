import re
from functools import cache

def parse(input: str) -> list[str]:
    return [
        s.strip() for s in input.strip().split("\n")
    ]

def part1(input: str) -> int:
    """Solve part 1."""
    joltages = []
    for bank in parse(input):
        joltages.append(max([
            int(pos + bank[j])
            for i, pos in enumerate(bank)
            for j in range(i+1, len(bank))
        ]))
    return sum(joltages)

@cache
def max_jolt(s: str, count: int) -> int:
    if len(s) == 0 or count == 0:
        return None
    if len(s) == 1:
        return int(s)
    if count == 1:
        return max([
            int(s[i])
            for i in range(len(s))
        ])
    else:
        skip = max_jolt(s[1:], count)
        all = [skip]
        for i in range(len(s)-count+1):
            next = max_jolt(s[i+1:], count-1)
            all.append(int(s[i] + str(next if next else '')))
        return max(all)

def part2(input: str) -> int:
    """Solve part 2."""
    joltages = []
    for bank in parse(input):
        joltages.append(max_jolt(bank, 12))
    return sum(joltages)

if __name__ == "__main__":
    from lib.runner import run_day
    run_day(3, part1, part2)
