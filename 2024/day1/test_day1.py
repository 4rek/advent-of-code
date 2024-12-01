from .solution import part1, part2
import os

day = "1"

def test_part1_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo1.txt", "r")
    lines = f.readlines()

    assert part1(lines) == 11


def test_part1():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.readlines()

    assert part1(lines) == 2057374


def test_part2_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo2.txt", "r")
    lines = f.readlines()

    assert part2(lines) == 31


def test_part2():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.readlines()

    assert part2(lines) == 23177084
