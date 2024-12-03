from typing import List

import os

def part1(lines: List[str]):
    first = []
    second = []

    for line in lines:
        first.append(line.strip().split("   ")[0])
        second.append(line.strip().split("   ")[1])

    first = sorted(first)
    second = sorted(second)

    return sum(abs(int(second[i]) - int(first[i])) for i in range(len(first)))


def part2(lines: List[str]):
    first = []
    second = {}

    for line in lines:
        x = line.strip().split("   ")
        first.append(x[0])
        second[x[1]] = second.get(x[1], 0) + 1

    return sum(int(item) * second.get(item, 0) for item in first)


if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day1/inputs/main.txt", "r")
    lines = f.readlines()
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))
