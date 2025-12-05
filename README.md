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

## Project Structure

```
advent-of-code-2025/
├── aoc.py                 # CLI implementation
├── day01.py               # Day 1 solution
├── day01.txt              # Day 1 input
├── day01_example.txt      # Day 1 example input
├── test_day01.py          # Day 1 tests
├── day02.py               # Day 2 solution
└── ...
```

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

### Watch Mode (Auto-test on Save)

Watch files and automatically re-run tests when they change:
```bash
uv run ./aoc.py watch <day>
```

Example:
```bash
uv run ./aoc.py watch 5
```

This watches `day05.py`, `test_day05.py`, and `day05_example.txt` and runs tests whenever any of them change. Press Ctrl+C to stop.

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

## Typical Workflow

1. **Create files for a new day:**
   ```bash
   uv run ./aoc.py new 5
   ```

2. **Add example input from problem description:**
   - Copy example input from the problem → `day05_example.txt`
   - Copy actual input from browser → `day05.txt`

3. **Update test with expected answer:**
   - Edit `test_day05.py`
   - Replace `None` with the expected answer from the example
   - Remove `@pytest.mark.skip` decorator

4. **Start watch mode:**
   ```bash
   uv run ./aoc.py watch 5
   ```

5. **Implement solution:**
   - Edit `day05.py`
   - Implement `part1()` function
   - Tests run automatically on save
   - Iterate until tests pass

6. **Run against actual input:**
   ```bash
   uv run ./aoc.py run 5
   ```

7. **Repeat for part 2:**
   - Update `test_part2` with expected answer
   - Remove `@pytest.mark.skip` decorator
   - Implement `part2()` function
   - Run solution again

## File Templates

### Solution File (`dayNN.py`)

```python
def part1(input_data: str) -> int:
    """Solve part 1."""
    pass


def part2(input_data: str) -> int:
    """Solve part 2."""
    pass


if __name__ == "__main__":
    with open("dayNN.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
```

### Test File (`test_dayNN.py`)

```python
import pytest
from dayNN import part1, part2


@pytest.fixture
def example_input():
    """Load example input from file."""
    with open("dayNN_example.txt") as f:
        return f.read()


@pytest.mark.skip(reason="Not implemented yet")
def test_part1(example_input):
    """Test part 1 with example input."""
    assert part1(example_input) == None  # Replace None with expected value


@pytest.mark.skip(reason="Not implemented yet")
def test_part2(example_input):
    """Test part 2 with example input."""
    assert part2(example_input) == None  # Replace None with expected value
```

## Dependencies

- Python 3.13+
- pytest - Testing framework
- pytest-watcher - File watching for auto-testing
