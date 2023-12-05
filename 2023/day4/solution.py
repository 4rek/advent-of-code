from typing import List
import os


def part1(lines: List[str]):
    result = 0
    for line in lines:
        numbers = line.strip().split(":")[1].strip().split("|")
        winning = list(filter(len, numbers[0].strip().split(" ")))
        having = list(filter(len, numbers[1].strip().split(" ")))

        local_result = -1 + sum(h in winning for h in having)
        if local_result > -1:
            result += 2 ** (local_result)

    return result


def part2(lines: List[str]):
    d = {i: {"wins": 0, "count": 1} for i in range(len(lines))}

    for line_idx, line in enumerate(lines):
        numbers = line.strip().split(":")[1].strip().split("|")
        winning = list(filter(len, numbers[0].strip().split(" ")))
        having = list(filter(len, numbers[1].strip().split(" ")))

        local_result = sum(h in winning for h in having)
        d[line_idx]["wins"] = local_result

    s = 0

    for key, value in d.items():
        for x in range(key + 1, key + 1 + value["wins"]):
            d[x]["count"] += 1 * value["count"]
        s += value["count"]

    return s
