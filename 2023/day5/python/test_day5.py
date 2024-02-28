from .solution import part1, part2
import os

day = "5"


def test_part1_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo1.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 35


def test_part1():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 282277027


def test_part2_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo1.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 46


def test_part2():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 11554135
