def part1(input: str) -> int:
    """Solve part 1."""
    lines = input.rstrip().split("\n")
    value = 50
    count = 0
    for line in lines:
        v = int(line.replace("L", "-").replace("R", "+"))
        value = (100 + value + v) % 100
        if (value == 0):
            count = count + 1
    return count

def part2(input: str) -> int:
    """Solve part 2."""
    lines = input.rstrip().split("\n")
    value = 50
    count = 0
    for line in lines:
        sgn = -1 if line[0] == "L" else 1
        v = int(line[1:])
        full = v // 100
        rest = v % 100
        count += full
        new_value = value + sgn*rest
        if (value != 0 and (new_value <= 0 or new_value > 99)):
            count += 1
        value = new_value % 100
    return count


if __name__ == "__main__":
    from lib.runner import run_day
    run_day(1, part1, part2)
