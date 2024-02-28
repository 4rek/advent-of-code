import os
from time import process_time_ns


def get_sum_for_given_offset(n, offset):
    k = list(offset.keys())
    return sum(offset[i] for i in range(k[0], n + 1) if i in offset)


def get_galaxies_coordinates(data, offset_x, offset_y):
    m = {}
    counter = 1

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "#":
                xc = x + get_sum_for_given_offset(x, offset_x)
                yc = y + get_sum_for_given_offset(y, offset_y)
                m[counter] = [xc, yc]
                counter += 1

    return m


def expand_data(data, c):
    offset_y = {i: c for i, row in enumerate(data) if row.count(".") == len(row)}

    data = list(map(list, zip(*data)))

    offset_x = {i: c for i, row in enumerate(data) if row.count(".") == len(row)}
    return offset_x, offset_y


def part1(lines: str):
    data = list(map(lambda x: list(x), lines.splitlines()))

    x, y = expand_data(data, 1)
    m = get_galaxies_coordinates(data, x, y)

    s = 0

    keys = list(m.keys())

    for key in keys:
        for i in range(key + 1, keys[-1] + 1):
            s += abs(m[i][0] - m[key][0]) + abs(m[i][1] - m[key][1])

    return s


def part2(lines: str, test_c):
    data = list(map(lambda x: list(x), lines.splitlines()))

    x, y = expand_data(data, test_c - 1)
    m = get_galaxies_coordinates(data, x, y)

    s = 0

    keys = list(m.keys())

    for key in keys:
        for i in range(key + 1, keys[-1] + 1):
            s += abs(m[i][0] - m[key][0]) + abs(m[i][1] - m[key][1])

    return s


def main():
    time_start = process_time_ns()
    f = open(f"{os.getcwd()}/day11/inputs/main.txt", "r")
    lines = f.read().strip()
    # print(part1(lines))
    print(part2(lines, 1000000))
    time_end = process_time_ns()
    time_duration = time_end - time_start
    print(f"Took {time_duration} ns")


main()
