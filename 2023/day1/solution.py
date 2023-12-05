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
    
    sum = 0
    for r in result:
        sum += r

    return sum

def part2(lines: List[str]):
    dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    result = []

    for line in lines:
        local_result = []

        for match in re.finditer(r'\d', line):
            local_result.append([match.start(), int(match.group())])

        for word, number in dict.items():
            for match in re.finditer(word, line):
                local_result.append([match.start(), number])

        local_res = sorted(local_result, key=itemgetter(0))
        final_number = str(local_res[0][1]) + str(local_res[-1][1])
        result.append(int(final_number))
        
    return sum(result)
    