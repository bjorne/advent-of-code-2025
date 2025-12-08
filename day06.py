import operator
from functools import reduce

OPS = {
    '*': operator.mul,
    '+': operator.add,
}

def parse(input: str) -> (list[str], list[int]):
    lines = input.strip().split("\n")
    # equalize line lengths for simplicity
    max_len = max([len(line) for line in lines])
    lines = [line.ljust(max_len) for line in lines]
    column_spaces = [
        i
        for i in range(len(lines[0]))
        if all([line[i] == ' ' for line in lines])
    ]
    columns = [
        range(start, stop)
        for start, stop in zip([0] + column_spaces, column_spaces + [len(lines[0])])
    ]
    return lines, columns

def part1(input: str) -> int:
    """Solve part 1."""
    lines, columns = parse(input)
    results = []
    for col in columns:
        rows = list(map(lambda line: line[col.start:col.stop].strip(), lines))
        op = rows.pop()
        numbers = list(map(int, rows))
        results.append(reduce(OPS[op], numbers))

    return sum(results)
        

def part2(input: str) -> int:
    """Solve part 2."""
    lines, columns = parse(input)
    results = []
    for col in columns:
        numbers = []
        for i in reversed(col):
            digits = [d for line in lines[:-1] if (d := line[i]).strip() != '']
            if len(digits) > 0:
                numbers.append(int(''.join(digits)))
        op = lines[-1][col.start:col.stop].strip()
        results.append(reduce(OPS[op], numbers))
    return sum(results)


if __name__ == "__main__":
    from lib.runner import run_day
    run_day(6, part1, part2)
