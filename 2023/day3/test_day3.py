from .solution import part1, part2
import os

def test_part1_demo():
    f = open(os.getcwd() + '/day3/inputs/demo1.txt', 'r')
    lines = f.readlines()

    assert part1(lines) == 4361

def test_part1():
    f = open(os.getcwd() + '/day3/inputs/main.txt', 'r')
    lines = f.readlines()

    assert part1(lines) == 527364

def test_part2_demo():
    f = open(os.getcwd() + '/day3/inputs/demo2.txt', 'r')
    lines = f.readlines()

    assert part2(lines) == 467835

def test_part2():
    f = open(os.getcwd() + '/day3/inputs/main.txt', 'r')
    lines = f.readlines()

    assert part2(lines) == 79026871
