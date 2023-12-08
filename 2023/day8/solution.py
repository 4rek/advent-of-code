import os
from time import process_time_ns
from math import lcm


def get_steps_counter(directions, d, k) -> int:
    counter = 0
    direction_key = -1

    while not k.endswith("Z"):
        counter += 1

        direction_key = direction_key + 1 if len(directions) > direction_key + 1 else 0
        direction = directions[direction_key]

        k = d[k][direction]

    return counter


def part1(lines: str):
    data = lines.split("\n")
    directions = [1 if i == "R" else 0 for i in data[0]]

    d = {}

    for line in data[2:]:
        key, value = (
            line.replace(" ", "", -1).replace("(", "").replace(")", "").split("=")
        )
        d[key] = value.split(",")

    return get_steps_counter(directions, d, "AAA")


def part2(lines: str):
    data = lines.split("\n")
    directions = [1 if i == "R" else 0 for i in data[0]]

    d = {}

    starting_points = []

    for line in data[2:]:
        key, value = (
            line.replace(" ", "", -1).replace("(", "").replace(")", "").split("=")
        )
        d[key] = value.split(",")

        if key.endswith("A"):
            starting_points.append(key)

    results = [get_steps_counter(directions, d, p) for p in starting_points]

    return lcm(*results)


# def main():
#     time_start = process_time_ns()
#     f = open(f"{os.getcwd()}/day8/inputs/main.txt", "r")
#     lines = f.read().strip()
#     print(part2(lines))
#     time_end = process_time_ns()
#     time_duration = time_end - time_start
#     print(f"Took {time_duration} ns")


# main()
