#!/usr/bin/env python3
"""Advent of Code 2025 CLI tool."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Find uv in PATH or common locations
UV = None
for path in [os.path.expanduser("~/.local/bin/uv"), "uv"]:
    try:
        result = subprocess.run([path, "--version"], capture_output=True, check=True)
        UV = path
        break
    except (FileNotFoundError, subprocess.CalledProcessError):
        continue

if UV is None:
    print("❌ uv not found. Please install uv.")
    sys.exit(1)


def create_new_day(day: int) -> None:
    """Create files for a new day."""
    day_str = f"{day:02d}"
    
    # Create day implementation file
    day_file = Path(f"day{day_str}.py")
    if day_file.exists():
        print(f"❌ {day_file} already exists")
        sys.exit(1)
    
    day_content = f'''def part1(input: str) -> int:
    """Solve part 1."""
    return 42


def part2(input: str) -> int:
    """Solve part 2."""
    pass


if __name__ == "__main__":
    from lib.runner import run_day
    run_day({day}, part1, part2)
'''
    day_file.write_text(day_content)
    print(f"✅ Created {day_file}")
    
    # Create test file
    test_file = Path(f"test_day{day_str}.py")
    test_content = f'''import pytest
from day{day_str} import part1, part2


@pytest.fixture
def example_input():
    """Load example input from file."""
    with open("day{day_str}_example.txt") as f:
        return f.read()


@pytest.mark.skip(reason="Not implemented yet")
def test_part1(example_input):
    """Test part 1 with example input."""
    assert part1(example_input) == None  # Replace None with expected value


@pytest.mark.skip(reason="Not implemented yet")
def test_part2(example_input):
    """Test part 2 with example input."""
    assert part2(example_input) == None  # Replace None with expected value
'''
    test_file.write_text(test_content)
    print(f"✅ Created {test_file}")
    
    # Create example input file
    example_file = Path(f"day{day_str}_example.txt")
    example_file.write_text("")
    print(f"✅ Created {example_file}")
    
    # Create empty input file
    input_file = Path(f"day{day_str}.txt")
    input_file.write_text("")
    print(f"✅ Created {input_file}")
    
    print(f"\n📝 Next steps:")
    print(f"   1. Add example input to day{day_str}_example.txt")
    print(f"   2. Add actual input to day{day_str}.txt")
    print(f"   3. Implement part1 and part2 in day{day_str}.py")
    print(f"   4. Update tests with expected values")


def run_tests(day: int = None) -> None:
    """Run tests for all days or a specific day."""
    cmd = [UV, "run", "pytest", "-v"]
    
    if day is not None:
        day_str = f"{day:02d}"
        test_file = f"test_day{day_str}.py"
        if not Path(test_file).exists():
            print(f"❌ {test_file} does not exist")
            sys.exit(1)
        cmd.append(test_file)
        print(f"🧪 Running tests for day {day}...")
    else:
        print("🧪 Running all tests...")
    
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


def run_solution(day: int) -> None:
    """Run a day's solution against its input."""
    day_str = f"{day:02d}"
    day_file = Path(f"day{day_str}.py")
    input_file = Path(f"day{day_str}.txt")
    
    if not day_file.exists():
        print(f"❌ {day_file} does not exist")
        sys.exit(1)
    
    if not input_file.exists():
        print(f"❌ {input_file} does not exist")
        sys.exit(1)
    
    print(f"🚀 Running solution for day {day}...")
    result = subprocess.run([UV, "run", "python", str(day_file)])
    sys.exit(result.returncode)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Advent of Code 2025 CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # new command
    new_parser = subparsers.add_parser("new", help="Create files for a new day")
    new_parser.add_argument("day", type=int, help="Day number (1-25)")
    
    # test command
    test_parser = subparsers.add_parser("test", help="Run tests")
    test_parser.add_argument("day", type=int, nargs="?", help="Specific day to test (optional)")
    
    # run command
    run_parser = subparsers.add_parser("run", help="Run a day's solution")
    run_parser.add_argument("day", type=int, help="Day number to run")
    
    args = parser.parse_args()
    
    if args.command == "new":
        create_new_day(args.day)
    elif args.command == "test":
        run_tests(args.day)
    elif args.command == "run":
        run_solution(args.day)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
