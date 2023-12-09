import os
from time import process_time_ns


def calculate_diffs(nums):
    return [nums[i + 1] - nums[i] for i in range(len(nums)) if i + 1 < len(nums)]


def get_next_number(nums):
    results = []

    tmp = calculate_diffs(nums)

    while any(i != tmp[0] for i in tmp):
        results.append(tmp)
        tmp = calculate_diffs(tmp)

    results.append(tmp + [tmp[0]])
    results.reverse()

    for idx in range(len(results)):
        if idx == 0:
            continue
        results[idx] = results[idx] + [results[idx][-1] + results[idx - 1][-1]]

    return nums[-1] + results[-1][-1]


def part1(lines: str):
    next_items = []
    for line in lines.splitlines():
        nums = list(map(int, line.split()))
        next_items.append(get_next_number(nums))

    return sum(next_items)


def part2(lines: str):
    next_items = []
    for line in lines.splitlines():
        nums = list(map(int, line.split()))
        next_items.append(get_next_number(nums[::-1]))

    return sum(next_items)


# def main():
#     time_start = process_time_ns()
#     f = open(f"{os.getcwd()}/day9/inputs/demo.txt", "r")
#     lines = f.read().strip()
#     print(part2(lines))
#     time_end = process_time_ns()
#     time_duration = time_end - time_start
#     print(f"Took {time_duration} ns")


# main()
