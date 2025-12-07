# Advent of Code 2025

Python solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

1. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone and enter the repository:
   ```bash
   cd advent-of-code-2025
   ```

3. Dependencies will be automatically installed when you run commands.

## Commands

All commands use `uv run ./aoc.py`:

### Create a New Day

```bash
uv run ./aoc.py new <day>
```

Creates three files for the specified day:
- `dayNN.py` - Solution file with `part1()` and `part2()` functions
- `test_dayNN.py` - Test file with pytest fixtures
- `dayNN_example.txt` - Example input file (empty, to be filled)
- `dayNN.txt` - Actual input file (empty, to be filled)

Example:
```bash
uv run ./aoc.py new 5
```

### Run Tests

Run all tests:
```bash
uv run ./aoc.py test
```

Run tests for a specific day:
```bash
uv run ./aoc.py test <day>
```

Example:
```bash
uv run ./aoc.py test 5
```

### Watch Mode

Watch files and automatically re-run tests when they change:
```bash
uv run ptw .
```

### Run Solution

Run a day's solution against its input file:
```bash
uv run ./aoc.py run <day>
```

Example:
```bash
uv run ./aoc.py run 5
```

This runs `day05.py` with input from `day05.txt` and prints the results.
