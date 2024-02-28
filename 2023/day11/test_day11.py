from .solution import part1, part2
import os

day = "11"


def test_part1_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 374


def test_part1():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 9974721


def test_part2_demo_times10():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part2(lines, 10) == 1030


def test_part2_demo_times100():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part2(lines, 100) == 8410


def test_part2():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part2(lines, 1000000) == 702770569197
