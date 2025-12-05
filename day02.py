import re

def parse(input: str) -> list[(int, int)]:
    return [
        [int(v) for v in s.strip().split("-")]
        for s in input.split(",")
    ]

def part1(input: str) -> int:
    """Solve part 1."""
    invalid = [
        v
        for start, stop in parse(input)
        for v in range(start, stop+1)
        if (s := str(v)) and len(s) % 2 == 0 and s[0:len(s)//2] == s[len(s)//2:]
    ]
    return sum(invalid)

def part2(input: str) -> int:
    """Solve part 2."""
    regex = re.compile(r'(.+)\1+$')
    invalid = [
        v
        for start, stop in parse(input)
        for v in range(start, stop+1)
        if (s := str(v)) and regex.match(s)
    ]
    return sum(invalid)


if __name__ == "__main__":
    with open("day02.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
