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

    s = 0
    for i in range(len(first)):
        s += abs(int(second[i]) - int(first[i]))

    print(s)
    return s


def part2(lines: List[str]):
    first = []
    second = {}
    
    for line in lines:
        x = line.strip().split("   ")
        first.append(x[0])
        second[x[1]] = second.get(x[1], 0) + 1

    s = 0    

    for i in range(len(first)):
        s += int(first[i]) * second.get(first[i], 0)
    
    return s


if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day1/inputs/main.txt", "r")
    lines = f.readlines()
    print("Part 2: ", part2(lines))
