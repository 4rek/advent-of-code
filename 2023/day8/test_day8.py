from .solution import part1, part2
import os

day = "8"


def test_part1_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 2


def test_part1_demo2():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo2.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 6


def test_part1():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 11309


def test_part2_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo3.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 6


def test_part2():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 13740108158591
