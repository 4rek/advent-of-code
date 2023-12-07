from .solution import part1, part2
import os
from time import process_time

day = "7"


def test_part1_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 6440


def test_part1():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 250453939


def test_part2_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 5905


def test_part2():
    # record start time
    time_start = process_time()
    # execute the statement
    ...

    # report the duration
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 248652697
    # record end time
    time_end = process_time()
    # calculate the duration
    time_duration = time_end - time_start
    print(f"Took {time_duration:.3f} seconds")
