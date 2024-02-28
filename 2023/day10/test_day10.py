from .solution import part1, part2
import pytest
import os

day = "10"


@pytest.mark.skip(reason="no way of currently testing this")
def test_part1_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 114


@pytest.mark.skip(reason="no way of currently testing this")
def test_part1():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part1(lines) == 2005352194


@pytest.mark.skip(reason="no way of currently testing this")
def test_part2_demo():
    f = open(f"{os.getcwd()}/day{day}/inputs/demo.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 2


@pytest.mark.skip(reason="no way of currently testing this")
def test_part2():
    f = open(f"{os.getcwd()}/day{day}/inputs/main.txt", "r")
    lines = f.read().strip()

    assert part2(lines) == 1077
