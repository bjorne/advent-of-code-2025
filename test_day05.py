import pytest
from day05 import part1, part2


@pytest.fixture
def example_input():
    """Load example input from file."""
    with open("day05_example.txt") as f:
        return f.read()


def test_part1(example_input):
    """Test part 1 with example input."""
    assert part1(example_input) == 3


def test_part2(example_input):
    """Test part 2 with example input."""
    assert part2(example_input) == 14
