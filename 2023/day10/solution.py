import os
from time import process_time_ns


def part1(lines: str):
    lines = lines.splitlines()

    s_coords = []

    for i in range(len(lines)):
        if "S" in lines[i]:
            s_coords = [i, lines[i].index("S")]

    print(s_coords)

    return 5


def part2(lines: str):
    return 2


def main():
    time_start = process_time_ns()
    f = open(f"{os.getcwd()}/day10/inputs/demo.txt", "r")
    lines = f.read().strip()
    print(part1(lines))
    time_end = process_time_ns()
    time_duration = time_end - time_start
    print(f"Took {time_duration} ns")


main()
