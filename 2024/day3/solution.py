from typing import List

import os
import re

def calculate(s: str) -> int:
    matches = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', s)
    result = [int(x)*int(y) for x, y in matches]
    return sum(result)


def part1(lines: List[str]):
    r = "".join(lines)
    return calculate(r)

def part2(lines: List[str]):
    r = "".join(lines).split("do()")
    z = "".join(i.split("don't()")[0] for i in r)
    return calculate(z)


if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day3/inputs/main.txt", "r")
    lines = f.readlines()
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))