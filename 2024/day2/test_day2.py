from .solution import part1, part2
import os

day = "2"

def test_part1_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo1.txt", "r")
    lines = f.readlines()

    assert part1(lines) == 2


def test_part1():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.readlines()

    assert part1(lines) == 213


def test_part2_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo2.txt", "r")
    lines = f.readlines()

    assert part2(lines) == 4


def test_part2():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.readlines()

    assert part2(lines) == 285
