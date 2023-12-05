from typing import List

import re
from operator import itemgetter


def part1(lines: List[str]):
    result = []
    for line in lines:
        first = ""
        last = ""
        for ch in line:
            try:
                v = int(ch)
                first = ch if first == "" else first
                last = ch
            finally:
                continue
        num = int(first + last)
        result.append(num)

    return sum(result)


def part2(lines: List[str]):
    d = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    result = []

    for line in lines:
        local_result = [
            [match.start(), int(match.group())] for match in re.finditer(r"\d", line)
        ]
        for word, number in d.items():
            local_result.extend(
                [match.start(), number] for match in re.finditer(word, line)
            )
        local_res = sorted(local_result, key=itemgetter(0))
        final_number = str(local_res[0][1]) + str(local_res[-1][1])
        result.append(int(final_number))

    return sum(result)
