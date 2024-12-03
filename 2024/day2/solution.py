from typing import List

import os

def part1(lines: List[str]):
    safe_count = 0

    for line in lines:
        reports = list(map(int, line.strip().split(" ")))

        safe = is_safe(reports)
        if safe:
            safe_count += 1

    return safe_count

def part2(lines: List[str]):
    safe_count = 0

    for line in lines:
        reports = list(map(int, line.strip().split(" ")))

        safe = is_safe(reports)
        if safe:
            safe_count += 1
        else:
            for i in range(len(reports)):
                if is_safe(get_modified_report(reports, i)):
                    safe_count += 1
                    break

    return safe_count

def get_modified_report(reports: List[int], i: int) -> List[int]:
    new_list = list(reports)
    new_list.pop(i)
    return new_list

def is_safe(reports: List[int]) -> bool:
    direction = 0 if reports[1] == reports[0] else 1 if reports[1] > reports[0] else -1
    safe = True
    failed_at = []

    for idx, report in enumerate(reports):
        if idx == 0:
            continue

        if report == reports[idx - 1]:
            failed_at.append(idx)

        if abs(report - reports[idx - 1]) > 3:
            failed_at.append(idx)
        if direction == 1 and report < reports[idx - 1]:
            failed_at.append(idx)
        if direction == -1 and report > reports[idx - 1]:
            failed_at.append(idx)

    safe = len(failed_at) == 0

    return safe


if __name__ == "__main__":
    f = open(f"{os.getcwd()}/day2/inputs/main.txt", "r")
    lines = f.readlines()
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))