from .solution import part1, part2
import os

def test_part1_demo():
    f = open(os.getcwd() + '/day1/inputs/demo1.txt', 'r')
    lines = f.readlines()

    assert part1(lines) == 142

def test_part1():
    f = open(os.getcwd() + '/day1/inputs/main.txt', 'r')
    lines = f.readlines()

    assert part1(lines) == 54304

def test_part2_demo():
    f = open(os.getcwd() + '/day1/inputs/demo2.txt', 'r')
    lines = f.readlines()

    assert part2(lines) == 281

def test_part2():
    f = open(os.getcwd() + '/day1/inputs/main.txt', 'r')
    lines = f.readlines()

    assert part2(lines) == 54418
